## Remu-Operator

This is, a framework to separate the resolution of operator precedence and associativity from parsing time,
by using a concise algorithm instead of Shunting Yard algorithm.

[Taine Zhao](http://github.com/thautwarm) is the author of this algorithm, and has named it "Operator Bubbling".
 

```python
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
```
