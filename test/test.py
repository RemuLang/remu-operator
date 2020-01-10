from remu_operator import Operator, binop_reduce

precedences = {
    '+': 1,
    '*': 2,
    "^": 3,
}

left = False
right = True

associativities = {'+': left, '*': left, '^': right}


def cons(v):
    return lambda l, r: '({} {} {})'.format(l, v, r)


x = binop_reduce(
    cons,
    [1, Operator("+"), 2,
     Operator("*"), 3, Operator("^"), 4,
     Operator("^"), 5, Operator("+"), 6,
     Operator("*"), 7], precedences, associativities)

assert x == '((1 + (2 * (3 ^ (4 ^ 5)))) + (6 * 7))'
