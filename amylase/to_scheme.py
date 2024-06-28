import sys
from typing import List, Union, Tuple, Iterator


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
        return f"({ast.operator} {to_scheme(ast.arg1)} {to_scheme(ast.arg2)})"
    elif isinstance(ast, UnaryOperator):
        return f"({ast.operator} {to_scheme(ast.arg)})"
    elif isinstance(ast, If):
        return f"(if {to_scheme(ast.condition)} {to_scheme(ast.true)} {to_scheme(ast.false)})"
    elif isinstance(ast, Lambda):
        return f"(lambda (variable{ast.variable_name}) {to_scheme(ast.body)})"
    elif isinstance(ast, Variable):
        return f"variable{ast.name}"


def translate(program: str) -> str:
    tokens = tokenize(program)
    ast = parse(iter(tokens))
    return to_scheme(ast)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    args = parser.parse_args()
    with open(args.source_file) as f:
        source_code = f.read()
    result = translate(source_code)    
    print(result)


if __name__ == "__main__":
    main()
