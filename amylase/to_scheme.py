import sys
from typing import List, Union, Tuple, Iterator, Set


class Token:
    token: str

    def __init__(self, s: str):
        self.token = s

    @property
    def indicator(self) -> str:
        return self.token[0]

    @property
    def body(self) -> str:
        return self.token[1:]


def tokenize(program: str) -> List[Token]:
    return [Token(token_str) for token_str in program.split(" ")]


ASTNode = Union["BinaryApply", "BinaryOperator", "UnaryOperator", "If", "Lambda", "Variable", bool, int, str]


class BinaryApply:
    lambda_: ASTNode
    term: ASTNode

    def __init__(self, lambda_: ASTNode, term: ASTNode) -> None:
        self.lambda_ = lambda_
        self.term = term

    def __str__(self):
        return f"{self.__class__.__name__}({self.lambda_}, {self.term})"


class BinaryOperator:
    operator: str
    arg1: ASTNode
    arg2: ASTNode

    def __init__(self, operator: str, arg1: ASTNode, arg2: ASTNode) -> None:
        self.operator = operator
        self.arg1 = arg1
        self.arg2 = arg2
        
    def __str__(self):
        return f"{self.__class__.__name__}({self.operator}, {self.arg1}, {self.arg2})"


class UnaryOperator:
    operator: str
    arg: ASTNode

    def __init__(self, operator: str, arg: ASTNode) -> None:
        self.operator = operator
        self.arg = arg

    def __str__(self):
        return f"{self.__class__.__name__}({self.operator}, {self.arg})"


class If:
    condition: ASTNode
    true: ASTNode
    false: ASTNode

    def __init__(self, condition: ASTNode, true: ASTNode, false: ASTNode) -> None:
        self.condition = condition
        self.true = true
        self.false = false

    def __str__(self):
        return f"{self.__class__.__name__}({self.condition}, {self.true}, {self.false})"


class Lambda:
    variable_name: int
    body: ASTNode

    def __init__(self, variable_name: int, body: ASTNode) -> None:
        self.variable_name = variable_name
        self.body = body

    def __str__(self):
        return f"{self.__class__.__name__}({self.variable_name}, {self.body})"


class Variable:
    name: int

    def __init__(self, name: int) -> None:
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"
ENCODE_MAP = {c: i for i, c in enumerate(ORDER)}


def encode_string(s: str) -> str:
    return ''.join([chr(ENCODE_MAP[c] + 33) for c in s])


def decode_string(body: str) -> str:
    return ''.join(ORDER[ord(c) - 33] for c in body)


def decode_integer(body: str) -> int:
    value = 0
    for c in body:
        value = value * 94 + ord(c) - 33
    return value


def parse(tokens: Iterator[Token]) -> ASTNode:
    token = next(tokens)
    if token.indicator == "T":
        return True
    elif token.indicator == "F":
        return False
    elif token.indicator == "I":
        return decode_integer(token.body)
    elif token.indicator == "S":
        return decode_string(token.body)
    elif token.indicator == "U":
        arg = parse(tokens)
        return UnaryOperator(token.body, arg)
    elif token.indicator == "B":
        arg1 = parse(tokens)
        arg2 = parse(tokens)
        if token.body == "$":
            return BinaryApply(arg1, arg2)
        else:
            return BinaryOperator(token.body, arg1, arg2)
    elif token.indicator == "?":
        arg1 = parse(tokens)
        arg2 = parse(tokens)
        arg3 = parse(tokens)
        return If(arg1, arg2, arg3)
    elif token.indicator == "L":
        lambda_body = parse(tokens)
        return Lambda(decode_integer(token.body), lambda_body)
    elif token.indicator == "v":
        return Variable(decode_integer(token.body))
    else:
        raise ValueError(f"invalid indicator: {token.indicator}")


def to_scheme(ast: ASTNode) -> str:
    if isinstance(ast, bool):
        return "#t" if ast else "#f"
    elif isinstance(ast, int):
        return str(ast)
    elif isinstance(ast, str):
        return '"' + ast + '"'
    elif isinstance(ast, BinaryApply):
        return f"({to_scheme(ast.lambda_)} {to_scheme(ast.term)})"
    elif isinstance(ast, BinaryOperator):
        if ast.operator == ".":
            func = "string-append"
        elif ast.operator == "=":
            func = "equal?"
        elif ast.operator == "&":
            func = "and"
        elif ast.operator == "|":
            func = "or"
        elif ast.operator == "/":
            func = "quotient"
        elif ast.operator == "%":
            func = "remainder"
        elif ast.operator == "T":
            # https://docs.racket-lang.org/reference/strings.html#%28def._%28%28quote._~23~25kernel%29._substring%29%29
            return f"(substring {to_scheme(ast.arg2)} 0 {to_scheme(ast.arg1)})"
        elif ast.operator == "D":
            return f"(substring {to_scheme(ast.arg2)} {to_scheme(ast.arg1)})"
        else:
            func = ast.operator
        return f"({func} {to_scheme(ast.arg1)} {to_scheme(ast.arg2)})"
    elif isinstance(ast, UnaryOperator):
        if ast.operator == "!":
            func = "not"
        elif ast.operator == "#":
            func = "stoi"
        elif ast.operator == "$":
            func = "itos"
        else:
            func = ast.operator
        return f"({func} {to_scheme(ast.arg)})"
    elif isinstance(ast, If):
        return f"(if {to_scheme(ast.condition)} {to_scheme(ast.true)} {to_scheme(ast.false)})"
    elif isinstance(ast, Lambda):
        return f"(lambda (v{ast.variable_name}) {to_scheme(ast.body)})"
    elif isinstance(ast, Variable):
        return f"v{ast.name}"


def detect_free_variables(ast: ASTNode) -> Set[int]:
    free_variables = set()
    for variable in _detect_free_variables(ast, []):
        free_variables.add(variable)
    return free_variables


def _detect_free_variables(ast: ASTNode, bound_variables: List[int]) -> Iterator[int]:
    if isinstance(ast, bool):
        return
    elif isinstance(ast, int):
        return
    elif isinstance(ast, str):
        return
    elif isinstance(ast, BinaryApply):
        yield from _detect_free_variables(ast.lambda_, bound_variables)
        yield from _detect_free_variables(ast.term, bound_variables)
    elif isinstance(ast, BinaryOperator):
        yield from _detect_free_variables(ast.arg1, bound_variables)
        yield from _detect_free_variables(ast.arg2, bound_variables)
    elif isinstance(ast, UnaryOperator):
        yield from _detect_free_variables(ast.arg, bound_variables)
    elif isinstance(ast, If):
        yield from _detect_free_variables(ast.condition, bound_variables)
        yield from _detect_free_variables(ast.true, bound_variables)
        yield from _detect_free_variables(ast.false, bound_variables)
    elif isinstance(ast, Lambda):
        bound_variables.append(ast.variable_name)
        yield from _detect_free_variables(ast.body, bound_variables)
        bound_variables.pop()
    elif isinstance(ast, Variable):
        if ast.name not in bound_variables:
            yield ast.name
        return


def translate(program: str) -> str:
    tokens = tokenize(program)
    ast = parse(iter(tokens))
    return to_scheme(ast)


def main():
    import argparse
    import subprocess
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("-r", "--run", action="store_true", help="run scheme with gauche")
    parser.add_argument("-s", "--strict", action="store_true", help="use strict evaluation. if not specified, call-by-need is used (lazy racket).")
    args = parser.parse_args()
    with open(args.source_file) as f:
        source_code = f.read()
    result = translate(source_code)

    with open("lib.rkt") as f:
        library_code = f.read()
    free_variables = detect_free_variables(parse(iter(tokenize(source_code))))
    free_var_defs = " ".join(f"(define v{free_variable} null)" for free_variable in free_variables)
    scheme_code = library_code + free_var_defs + "\n(display " + result + ") (newline)"
    racket_language = "racket" if args.strict else "lazy"
    if args.run:
        with open("run.rkt", "w") as f:
            print(scheme_code, file=f)
        subprocess.call(f"racket -I {racket_language} run.rkt", shell=True)
    else:
        print(scheme_code)


if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000)
    main()
