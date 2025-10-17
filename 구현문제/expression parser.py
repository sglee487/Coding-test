import operator
from functools import reduce

# ---------- Lexer ----------
def tokenize(s: str):
    tokens = []
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            tokens.append(("NUM", int(s[i:j])))
            i = j
            continue
        if ch.isalpha():
            j = i
            while j < n and s[j].isalpha():
                j += 1
            tokens.append(("ID", s[i:j]))
            i = j
            continue
        if ch in "+-*/^(),":
            tokens.append((ch, ch))
            i += 1
            continue
        if ch in "{}[]":
            raise ValueError(f"Unsupported bracket: {ch}")
        raise ValueError(f"Unexpected character: {ch}")
    tokens.append(("EOF", None))
    return tokens

# ---------- Builtins ----------
def f_plus(*args):
    if not args: raise ValueError("plus needs >=1 arg")
    return sum(args)

def f_mul(*args):
    if not args: raise ValueError("mul needs >=1 arg")
    return reduce(operator.mul, args, 1)

def f_minus(*args):
    if len(args) == 1:   # unary
        return -args[0]
    if len(args) == 2:   # binary
        return args[0] - args[1]
    raise ValueError("minus needs 1 or 2 args")

def f_div(*args):
    if len(args) == 1:
        return 1 / args[0]
    if len(args) == 2:
        return args[0] / args[1]
    raise ValueError("div needs 1 or 2 args")

BUILTINS = {
    "plus":  f_plus,
    "mul":   f_mul,
    "minus": f_minus,
    "div":   f_div,
}

# ---------- Parser/Evaluator (recursive descent) ----------
class Parser:
    def __init__(self, tokens):
        self.toks = tokens
        self.pos = 0

    def cur(self):
        return self.toks[self.pos]

    def eat(self, kind=None):
        tok = self.cur()
        if kind and tok[0] != kind and tok[1] != kind:
            raise ValueError(f"Expected {kind}, got {tok}")
        self.pos += 1
        return tok

    # expr := term (('+'|'-') term)*
    def parse_expr(self):
        val = self.parse_term()
        while True:
            t = self.cur()
            if t[0] == '+' or t[1] == '+':
                self.eat('+')
                val = val + self.parse_term()
            elif t[0] == '-' or t[1] == '-':
                self.eat('-')
                val = val - self.parse_term()
            else:
                break
        return val

    # term := power (('*'|'/') power)*
    def parse_term(self):
        val = self.parse_power()
        while True:
            t = self.cur()
            if t[0] == '*' or t[1] == '*':
                self.eat('*')
                val = val * self.parse_power()
            elif t[0] == '/' or t[1] == '/':
                self.eat('/')
                val = val / self.parse_power()
            else:
                break
        return val

    # power := unary ('^' power)?   # right-associative
    def parse_power(self):
        left = self.parse_unary()
        t = self.cur()
        if t[0] == '^' or t[1] == '^':
            self.eat('^')
            right = self.parse_power()
            return left ** right
        return left

    # unary := '-' unary | factor
    def parse_unary(self):
        t = self.cur()
        if t[0] == '-' or t[1] == '-':
            self.eat('-')
            return -self.parse_unary()
        return self.parse_factor()

    # factor := NUM | '(' expr ')' | func_call
    # func_call := ID '(' [expr (',' expr)*] ')'
    def parse_factor(self):
        t = self.cur()
        if t[0] == 'NUM':
            self.eat()
            return t[1]
        if t[0] == 'ID':
            name = t[1]
            self.eat('ID')
            # function call?
            if self.cur()[0] == '(' or self.cur()[1] == '(':
                self.eat('(')
                args = []
                if not (self.cur()[0] == ')' or self.cur()[1] == ')'):
                    args.append(self.parse_expr())
                    while self.cur()[0] == ',' or self.cur()[1] == ',':
                        self.eat(',')
                        args.append(self.parse_expr())
                self.eat(')')
                fn = BUILTINS.get(name)
                if not fn:
                    raise ValueError(f"Unknown function: {name}")
                return fn(*args)
            else:
                raise ValueError(f"Identifier '{name}' not callable here")
        if t[0] == '(' or t[1] == '(':
            self.eat('(')
            val = self.parse_expr()
            self.eat(')')
            return val
        raise ValueError(f"Unexpected token: {t}")

def evaluate(s: str) -> float:
    parser = Parser(tokenize(s))
    val = parser.parse_expr()
    if parser.cur()[0] != 'EOF':
        raise ValueError("Trailing junk")
    return val

# ---- quick demo ----
if __name__ == "__main__":
    expr = "plus(plus(2,3),5) + mul(minus(5,2),plus(3,3))"
    print(evaluate(expr))  # 28
