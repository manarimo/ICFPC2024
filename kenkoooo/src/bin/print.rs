use std::io::stdin;

const ORDER: &str = r###"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`|~ 
 "###;

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();

    let mut tokens = vec![];
    for token in input.trim().split_whitespace() {
        let bytes = token.as_bytes();
        match bytes[0] {
            b'T' => tokens.push(Token::True),
            b'F' => tokens.push(Token::False),
            b'I' => {
                tokens.push(Token::Integer(decode_int(&bytes[1..])));
            }
            b'S' => {
                let mut value = String::new();
                for &c in &bytes[1..] {
                    value.push(ORDER.as_bytes()[(c - 33) as usize] as char);
                }
                tokens.push(Token::String(value));
            }
            b'U' => tokens.push(Token::UnaryOperator(bytes[1] as char)),
            b'B' => tokens.push(Token::BinaryOperator(bytes[1] as char)),
            b'?' => tokens.push(Token::If),
            b'L' => tokens.push(Token::Lambda(decode_int(&bytes[1..]))),
            b'v' => tokens.push(Token::Variable(decode_int(&bytes[1..]))),
            _ => unreachable!("Unknown token: {}", token),
        }
    }

    let (root, rest) = parse(&tokens);
    eprintln!("{:?}", tokens);
    assert!(rest.is_empty());

    println!("{}", to_string(&root));
}

fn to_string(node: &Node) -> String {
    match node {
        Node::Bool(b) => b.to_string(),
        Node::Int(i) => i.to_string(),
        Node::Str(s) => format!("\"{}\"", s),
        Node::UnaryOp { op, operand } => format!("{}({})", op, to_string(operand)),
        Node::BinaryOp { op, lhs, rhs } => match op {
            '+' | '-' | '*' | '/' | '%' | '<' | '>' => {
                format!("({} {} {})", to_string(lhs), op, to_string(rhs))
            }
            '=' | '|' | '&' => {
                format!("({} {}{} {})", to_string(lhs), op, op, to_string(rhs))
            }
            '.' => {
                format!("({} + {})", to_string(lhs), to_string(rhs))
            }
            'T' => {
                format!("{}.substr(0, {})", to_string(rhs), to_string(lhs))
            }
            'D' => {
                format!("{}.substr({})", to_string(rhs), to_string(lhs))
            }
            '$' => {
                format!("{}({})", to_string(lhs), to_string(rhs))
            }
            _ => unreachable!("Unknown binary operator: {}", op),
        },
        Node::If { cond, then, else_ } => format!(
            "({} ? {} : {})",
            to_string(cond),
            to_string(then),
            to_string(else_)
        ),
        Node::Lambda { param, body } => format!("(v{} => {})", param, to_string(body)),
        Node::Variable(i) => format!("v{}", i),
    }
}

fn parse(tokens: &[Token]) -> (Node, &[Token]) {
    match &tokens[0] {
        Token::True => (Node::Bool(true), &tokens[1..]),
        Token::False => (Node::Bool(false), &tokens[1..]),
        Token::Integer(i) => (Node::Int(*i), &tokens[1..]),
        Token::String(s) => (Node::Str(s), &tokens[1..]),
        Token::UnaryOperator(op) => {
            let (operand, rest) = parse(&tokens[1..]);
            (
                Node::UnaryOp {
                    op: *op,
                    operand: Box::new(operand),
                },
                rest,
            )
        }
        Token::BinaryOperator(op) => {
            let (lhs, rest) = parse(&tokens[1..]);
            let (rhs, rest) = parse(rest);
            (
                Node::BinaryOp {
                    op: *op,
                    lhs: Box::new(lhs),
                    rhs: Box::new(rhs),
                },
                rest,
            )
        }
        Token::If => {
            let (cond, rest) = parse(&tokens[1..]);
            let (then, rest) = parse(rest);
            let (else_, rest) = parse(rest);
            (
                Node::If {
                    cond: Box::new(cond),
                    then: Box::new(then),
                    else_: Box::new(else_),
                },
                rest,
            )
        }
        Token::Lambda(i) => {
            let (body, rest) = parse(&tokens[1..]);
            (
                Node::Lambda {
                    param: *i,
                    body: Box::new(body),
                },
                rest,
            )
        }
        Token::Variable(i) => (Node::Variable(*i), &tokens[1..]),
    }
}

fn decode_int(bytes: &[u8]) -> i64 {
    let mut value = 0;
    for &c in bytes {
        value = value * 94 + (c - 33) as i64;
    }
    value
}

#[derive(Debug)]
enum Token {
    True,
    False,
    Integer(i64),
    String(String),
    UnaryOperator(char),
    BinaryOperator(char),
    If,
    Lambda(i64),
    Variable(i64),
}

#[derive(Debug, Clone)]
enum Node<'a> {
    Bool(bool),
    Int(i64),
    Str(&'a String),
    UnaryOp {
        op: char,
        operand: Box<Node<'a>>,
    },
    BinaryOp {
        op: char,
        lhs: Box<Node<'a>>,
        rhs: Box<Node<'a>>,
    },
    If {
        cond: Box<Node<'a>>,
        then: Box<Node<'a>>,
        else_: Box<Node<'a>>,
    },
    Lambda {
        param: i64,
        body: Box<Node<'a>>,
    },
    Variable(i64),
}
