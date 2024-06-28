pub mod eval;
pub mod tree;

pub fn encode_tokens(token: &Token) -> String {
    match token {
        Token::True => "T".to_string(),
        Token::False => "F".to_string(),
        Token::Int(n) => format!("I{}", encode_int(*n)),
        Token::Str(s) => format!("S{}", encode_str(&s)),
        Token::Unary(op) => format!("U{}", encode_unary_op(*op)),
        Token::Binary(op) => format!("B{}", encode_binary_op(*op)),
        Token::If => "?".to_string(),
        Token::Lambda(n) => format!("L{}", encode_int(*n)),
        Token::Var(n) => format!("v{}", encode_int(*n)),
    }
}
fn encode_int(n: i128) -> String {
    let mut s = String::new();
    let mut n = n;
    while n > 0 {
        s.push((n % 94 + 33) as u8 as char);
        n /= 94;
    }
    s.chars().rev().collect()
}
fn encode_str(s: &str) -> String {
    s.chars()
        .map(|c| (ORDER.find(c).unwrap() + 33) as u8 as char)
        .collect()
}
fn encode_unary_op(op: UnaryOp) -> char {
    match op {
        UnaryOp::Neg => '-',
        UnaryOp::Not => '!',
        UnaryOp::ToInt => '#',
        UnaryOp::ToStr => '$',
    }
}
fn encode_binary_op(op: BinaryOp) -> char {
    match op {
        BinaryOp::Add => '+',
        BinaryOp::Sub => '-',
        BinaryOp::Mul => '*',
        BinaryOp::Div => '/',
        BinaryOp::Mod => '%',
        BinaryOp::LessThan => '<',
        BinaryOp::GreaterThan => '>',
        BinaryOp::Equal => '=',
        BinaryOp::Or => '|',
        BinaryOp::And => '&',
        BinaryOp::Concat => '.',
        BinaryOp::Take => 'T',
        BinaryOp::Drop => 'D',
        BinaryOp::Lambda => '$',
    }
}

pub fn parse_token(token: &[u8]) -> Token {
    match token[0] {
        b'T' => Token::True,
        b'F' => Token::False,
        b'I' => Token::Int(parse_int(&token[1..])),
        b'S' => Token::Str(parse_str(&token[1..])),
        b'U' => Token::Unary(parse_unary_op(token[1])),
        b'B' => Token::Binary(parse_binary_op(token[1])),
        b'?' => Token::If,
        b'L' => Token::Lambda(parse_int(&token[1..])),
        b'v' => Token::Var(parse_int(&token[1..])),
        _ => unreachable!(),
    }
}

fn parse_int(body: &[u8]) -> i128 {
    let mut n = 0;
    for &c in body {
        n = n * 94 + c as i128 - 33;
    }
    n
}

const ORDER: &str = r###"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`|~ 
"###;

fn parse_str(body: &[u8]) -> String {
    let mut s = String::new();
    for &c in body {
        s.push(ORDER.as_bytes()[c as usize - 33] as char);
    }
    s
}

fn parse_unary_op(body: u8) -> UnaryOp {
    match body {
        b'-' => UnaryOp::Neg,
        b'!' => UnaryOp::Not,
        b'#' => UnaryOp::ToInt,
        b'$' => UnaryOp::ToStr,
        _ => unreachable!(),
    }
}

fn parse_binary_op(body: u8) -> BinaryOp {
    match body {
        b'+' => BinaryOp::Add,
        b'-' => BinaryOp::Sub,
        b'*' => BinaryOp::Mul,
        b'/' => BinaryOp::Div,
        b'%' => BinaryOp::Mod,
        b'<' => BinaryOp::LessThan,
        b'>' => BinaryOp::GreaterThan,
        b'=' => BinaryOp::Equal,
        b'|' => BinaryOp::Or,
        b'&' => BinaryOp::And,
        b'.' => BinaryOp::Concat,
        b'T' => BinaryOp::Take,
        b'D' => BinaryOp::Drop,
        b'$' => BinaryOp::Lambda,
        _ => unreachable!(),
    }
}

#[derive(Debug, Clone)]
pub enum Token {
    True,
    False,
    Int(i128),
    Str(String),
    Unary(UnaryOp),
    Binary(BinaryOp),
    If,
    Lambda(i128),
    Var(i128),
}

#[derive(Debug, Clone, Copy)]
pub enum UnaryOp {
    Neg,
    Not,
    ToInt,
    ToStr,
}

#[derive(Debug, Clone, Copy)]
pub enum BinaryOp {
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    LessThan,
    GreaterThan,
    Equal,
    Or,
    And,
    Concat,
    Take,
    Drop,
    Lambda,
}
