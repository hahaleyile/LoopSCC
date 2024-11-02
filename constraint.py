import copy
from enum import Enum, auto


class Comparison(Enum):
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_THAN_OR_EQUAL = auto()
    GREATER_THAN_OR_EQUAL = auto()


comparison_symbols = {
    Comparison.EQUAL: "==",
    Comparison.NOT_EQUAL: "!=",
    Comparison.LESS_THAN: "<",
    Comparison.GREATER_THAN: ">",
    Comparison.LESS_THAN_OR_EQUAL: "<=",
    Comparison.GREATER_THAN_OR_EQUAL: ">="
}


class Constraint:
    def __init__(self, lvalue, comparison: Comparison, rvalue):
        # constraint is not like assign, it left value can be any type
        self.lvalue = copy.deepcopy(lvalue)
        self.rvalue = copy.deepcopy(rvalue)
        self.comparison = comparison

    def __repr__(self):
        return str(self.lvalue) + " " + comparison_symbols[self.comparison] + " " + str(self.rvalue)

    def reverse(self):
        match self.comparison:
            case Comparison.EQUAL:
                return Constraint(self.lvalue, Comparison.NOT_EQUAL, self.rvalue)
            case Comparison.NOT_EQUAL:
                return Constraint(self.lvalue, Comparison.EQUAL, self.rvalue)
            case Comparison.LESS_THAN:
                return Constraint(self.lvalue, Comparison.GREATER_THAN_OR_EQUAL, self.rvalue)
            case Comparison.GREATER_THAN:
                return Constraint(self.lvalue, Comparison.LESS_THAN_OR_EQUAL, self.rvalue)
            case Comparison.LESS_THAN_OR_EQUAL:
                return Constraint(self.lvalue, Comparison.GREATER_THAN, self.rvalue)
            case Comparison.GREATER_THAN_OR_EQUAL:
                return Constraint(self.lvalue, Comparison.LESS_THAN, self.rvalue)
