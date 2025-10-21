import operator
from functools import reduce


def tokenize(s: str):
    tokens = []
    i = 0
    while i < len(s):
        if s[i].isspace():
            i += 1
            continue
        if s[i].isalpha():
            j = i
            while j < len(s) and s[j].isalpha():
                j += 1
            tokens.append(("OPERATOR", s[i:j]))
            i = j
            continue
        if s[i] in "+/*-^(),":
            tokens.append((s[i], s[i]))
            i += 1
            continue
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(("NUM", int(s[i:j])))
            i = j
            continue
    tokens.append(("EOF", None))
    return tokens


def f_plus(*args):
    return sum(args)


def f_mul(*args):
    return reduce(operator.mul, args, 1)


def f_minus(*args):
    if len(args) == 1:  # unary
        return -args[0]
    if len(args) == 2:  # binary
        return args[0] - args[1]
    return args[0] - args[1]


def f_div(*args):
    if len(args) == 1:
        return 1 / args[0]
    if len(args) == 2:
        return args[0] / args[1]
    raise ValueError("div needs 1 or 2 args")


BUILTINS = {
    "plus": f_plus,
    "mul": f_mul,
    "minus": f_minus,
    "div": f_div,
}


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def cur(self):
        return self.tokens[self.pos]

    def eat(self, kind=None):
        tok = self.cur()
        if kind and tok[0] != kind and tok[1] != kind:
            raise ValueError()
        self.pos += 1
        return tok

    # 순서: +-, /*, ^, -, ()

    def parse_expr(self):
        val = self.parse_term()
        while True:
            t = self.cur()
            if t[1] == '+':
                self.eat('+')
                right = self.parse_term()
                val = val + right
            elif t[1] == '-':
                self.eat('-')
                right = self.parse_term()
                val = val - right
            else:
                break
        return val

    def parse_term(self):
        val = self.parse_power()
        while True:
            t = self.cur()
            if t[1] == '*':
                self.eat('*')
                right = self.parse_power()
                val = reduce(operator.mul, val, right)
            elif t[1] == '/':
                self.eat('/')
                right = self.parse_power()
                val = val / right
            else:
                break
        return val

    def parse_power(self):
        val = self.parse_unary()
        t = self.cur()
        if t[1] == '^':
            self.eat('^')
            right = self.parse_expr()
            return val ** right
        return val

    def parse_unary(self):
        t = self.cur()
        if t[1] == '-':
            self.eat('-')
            return -self.parse_unary()
        return self.parse_factor()

    def parse_factor(self):
        t = self.cur()
        if t[0] == 'NUM':
            self.eat()
            return t[1]
        if t[0] == 'OPERATOR':

            f_val = BUILTINS.get(t[1])
            self.eat()
            t = self.cur()
            if t[0] == '(' or t[1] == '(':
                self.eat('(')
                args = []
                t = self.cur()
                if t[1] != ')':
                    args.append(self.parse_expr())
                    if self.cur()[0] == ',':
                        self.eat(',')
                        args.append(self.parse_expr())
                self.eat(')')
                return f_val(*args)
            else:
                raise ValueError(f"{f_val}")

        if t[0] in '(':
            self.eat('(')
            val = self.parse_expr()
            self.eat(')')
            return val
        raise ValueError(f"{t}")

    def evaluate(self):

        return self.parse_expr()


def evaluate(expr: str):
    my_parser = Parser(tokenize(expr))
    print(my_parser.tokens)
    return my_parser.evaluate()


# ---- quick demo ----
if __name__ == "__main__":
    expr = "plus(plus(2,3),5) + mul(minus(5,2),plus(3,3))"
    print(evaluate(expr))  # 28
