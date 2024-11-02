import copy

import z3

from constraint import Constraint, Comparison


class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class INT:
    # form: (ax+b)/c
    def __init__(self):
        self.symbol_num: int = 0
        self.symbol_index: dict[str:int] = dict()
        self.symbols: list[Symbol] = []
        self.addends: int = 0
        self.multipliers: list[int] = []
        # self.divisors = []

    @classmethod
    def define_int(cls, value: str):
        new_int = INT()
        new_int.symbol_num = 1

        symbol = Symbol(value)
        new_int.symbol_index[value] = 0
        new_int.symbols.append(symbol)
        new_int.addends = 0
        new_int.multipliers.append(1)
        return new_int

    # return int1 plus int2
    @classmethod
    def extend_int(cls, int1, int2):
        new_int = INT()
        new_int.addends = int1.addends + int2.addends

        def add_symbol(new, old, index):
            new.symbols.append(old.symbols[index])
            new.multipliers.append(old.multipliers[index])
            new.symbol_index[old.symbols[index].name] = new.symbol_num
            new.symbol_num += 1

        for i in range(int1.symbol_num):
            add_symbol(new_int, int1, i)

        for i in range(int2.symbol_num):
            # two INT have same symbol name
            if int2.symbols[i].name in new_int.symbol_index:
                ind = new_int.symbol_index[int2.symbols[i].name]
                new_int.multipliers[ind] += int2.multipliers[i]
            else:
                add_symbol(new_int, int2, i)

        # remove the symbol with multiplier 0
        for symbol, multiplier in zip(new_int.symbols, new_int.multipliers):
            if multiplier == 0:
                new_int.symbol_num -= 1
                new_int.symbols.remove(symbol)
                new_int.multipliers.remove(multiplier)

        # rebuild symbol_index
        new_int.symbol_index = dict()
        for i in range(new_int.symbol_num):
            new_int.symbol_index[new_int.symbols[i].name] = i

        return new_int

    def eq(self, other):
        if self.addends != other.addends:
            return False
        if self.symbol_num != other.symbol_num:
            return False
        for symbol in self.symbols:
            index1 = self.symbol_index[symbol.name]
            index2 = other.symbol_index.get(symbol.name)
            if index2 is None:
                return False
            if self.multipliers[index1] != other.multipliers[index2]:
                return False
        return True

    def __add__(self, other):
        if type(other) is int:
            new_int = copy.deepcopy(self)
            new_int.addends += other
        elif type(other) is INT:
            new_int = INT.extend_int(self, other)
        else:
            raise NotImplemented
        return new_int

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) is int:
            new_int = copy.deepcopy(self)
            new_int.addends -= other
        elif type(other) is INT:
            reverse_int = -other
            new_int = INT.extend_int(self, reverse_int)
        else:
            raise NotImplemented
        return new_int

    def __rsub__(self, other):
        if type(other) is int:
            new_int = -self
            new_int.addends += other
        elif type(other) is INT:
            reverse_int = -self
            new_int = INT.extend_int(other, reverse_int)
        else:
            raise NotImplemented
        return new_int

    def __mul__(self, other):
        if type(other) is int:
            new_int = copy.deepcopy(self)
            new_int.addends *= other
            for i in range(new_int.symbol_num):
                new_int.multipliers[i] *= other
        elif type(other) is INT:
            if other.symbol_num < 1:
                raise NotImplemented
            new_int = MUL_INT()
            new_int = new_int * self
            new_int = new_int * other
            return new_int
        else:
            raise NotImplemented
        return new_int

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.EQUAL, other)

    def __ne__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.NOT_EQUAL, other)

    def __lt__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.LESS_THAN, other)

    def __gt__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.GREATER_THAN, other)

    def __le__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.LESS_THAN_OR_EQUAL, other)

    def __ge__(self, other):
        return Constraint(copy.deepcopy(self), Comparison.GREATER_THAN_OR_EQUAL, other)

    def __neg__(self):
        reverse_int: INT = copy.deepcopy(self)
        reverse_int.addends = -reverse_int.addends
        for i in range(reverse_int.symbol_num):
            reverse_int.multipliers[i] = -reverse_int.multipliers[i]
        return reverse_int

    def __repr__(self):
        result = ""
        prefix = ""
        for i in range(self.symbol_num):
            if self.multipliers[i] > 0:
                if self.multipliers[i] != 1:
                    result += f"{prefix}{self.multipliers[i]}*{self.symbols[i].name}"
                else:
                    result += f"{prefix}{self.symbols[i].name}"
                if i == 0:
                    prefix = "+"
            elif self.multipliers[i] < 0:
                if self.multipliers[i] != -1:
                    result += f"{self.multipliers[i]}*{self.symbols[i].name}"
                else:
                    result += f"-{self.symbols[i].name}"

        if self.addends != 0:
            if self.addends > 0:
                result += f"+{self.addends}"
            else:
                result += f"{self.addends}"

        return result

    def update(self, value):
        if type(value) is INT:
            self.addends = value.addends
            self.symbol_num = value.symbol_num
            self.multipliers = value.multipliers.copy()
            self.symbols = value.symbols.copy()
            self.symbol_index = value.symbol_index.copy()


class MUL_INT:
    def __init__(self):
        self.dimension = 0
        self.multipliers: list[INT] = []
        self.base_int: INT = INT()

    def __repr__(self):
        result = ""
        if self.dimension > 0:
            for i in range(self.dimension - 1):
                result += f"({self.multipliers[i]}) * "
            result += f"({self.multipliers[self.dimension - 1]})"
        if self.base_int.symbol_num > 0:
            result += f" + {self.base_int}"
        return result

    def __mul__(self, other):
        if type(other) is INT:
            new_int = copy.deepcopy(self)
            new_int.dimension += 1
            new_int.multipliers.append(other)
            return new_int
        else:
            raise NotImplemented

    def __add__(self, other):
        if type(other) is INT or type(other) is int:
            new_int = copy.deepcopy(self)
            new_int.base_int = new_int.base_int + other
            return new_int
        else:
            raise NotImplemented

    def to_z3(self, symbols: dict[str, z3.Int]):
        def INT_to_z3(a: INT):
            result = []
            for i in range(a.symbol_num):
                if a.multipliers[i] != 1:
                    result.append(symbols[a.symbols[i].name] * a.multipliers[i])
                else:
                    result.append(symbols[a.symbols[i].name])
            if a.addends != 0:
                result.append(a.addends)
            return result

        if self.dimension < 1:
            raise Exception("dimension should be greater than 0")
        result = INT_to_z3(self.multipliers[0])
        for i in range(1, self.dimension):
            multiplier = INT_to_z3(self.multipliers[i])
            new_result = []
            for a in result:
                for b in multiplier:
                    new_result.append(a * b)
            result = new_result
        if len(result) < 1:
            raise Exception("result should not be empty")
        new_result = result[0]
        for i in range(1, len(result)):
            new_result += result[i]

        if self.base_int.symbol_num > 0:
            result = INT_to_z3(self.base_int)
            for i in range(len(result)):
                new_result += result[i]
        return new_result
