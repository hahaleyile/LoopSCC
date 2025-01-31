import copy
import z3

from int import INT, MUL_INT


class Assign:
    # two initialization methods
    # 1. use an instruction string to represent the assignment
    def __init__(self, instr=None, assign: tuple[INT, INT | MUL_INT] = None):
        self.instr = instr
        # lvalue represents the value after node, x'
        self.lvalue = None
        # rvalue represents the value before node, x0
        self.rvalue = None
        if assign is not None:
            if assign[0].symbol_num != 1 or assign[0].addends != 0 or assign[0].multipliers[0] != 1:
                raise Exception("lvalue should be a single symbol")
            self.lvalue = copy.deepcopy(assign[0])
            self.rvalue = copy.deepcopy(assign[1])

    def __repr__(self):
        if self.lvalue:
            return str(self.lvalue) + " = " + str(self.rvalue)
        elif self.instr == "":
            return str(self.instr)
        else:
            return "Error"

    def to_z3(self, lsymbols: dict[str, z3.Int], rsymbols: dict[str, z3.Int]):
        lvalue = self.lvalue.to_z3(lsymbols)
        rvalue = self.rvalue.to_z3(rsymbols)
        return lvalue == rvalue

    @classmethod
    # add new assignment expression to assignment list
    def merge_list(cls, assigns: list, assign):
        if assign is None or assign.rvalue is None:
            return

        new_assign = copy.deepcopy(assign)
        index = -1
        for i in range(len(assigns)):
            if assigns[i].lvalue.eq(assign.lvalue):
                index = i
                break

        if type(assign.rvalue) is INT:
            # calculate assign rvalue first, then replace new_assign's rvalue
            rvalue = INT()
            rvalue.addends = assign.rvalue.addends
            for symbol in assign.rvalue.symbols:
                exist = False
                for exist_assign in assigns:
                    if exist_assign.lvalue.eq(INT.define_int(symbol.name)):
                        rvalue = rvalue + exist_assign.rvalue * assign.rvalue.multipliers[
                            assign.rvalue.symbol_index[symbol.name]]
                        exist = True
                        break
                if not exist:
                    tmp = INT.define_int(symbol.name)
                    tmp = tmp * assign.rvalue.multipliers[assign.rvalue.symbol_index[symbol.name]]
                    rvalue = rvalue + tmp
            new_assign.rvalue = rvalue
        else:
            pass

        if index != -1:
            assigns[index] = new_assign
        else:
            assigns.append(new_assign)


class Node:
    def __init__(self):
        self.assigns: list[Assign] = []

    def __repr__(self):
        res = ""
        for i in range(len(self.assigns) - 1):
            res += str(self.assigns[i]) + "\\n"
        res += str(self.assigns[-1])
        return res
