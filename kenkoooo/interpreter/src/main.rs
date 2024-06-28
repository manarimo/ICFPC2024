use interpreter::{parse_token, Token};

fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();

    let tokens = buf
        .trim()
        .split_whitespace()
        .map(|token| parse_token(token.as_bytes()))
        .collect::<Vec<_>>();
    let (v, rest) = format(&tokens);
    println!("{v}");
    assert!(rest.is_empty());
}

fn format(tokens: &[Token]) -> (String, &[Token]) {
    match &tokens[0] {
        Token::True => ("true".into(), &tokens[1..]),
        Token::False => ("false".into(), &tokens[1..]),
        Token::Int(i) => (i.to_string(), &tokens[1..]),
        Token::Str(s) => (format!("\"{}\"", s), &tokens[1..]),
        Token::Unary(op) => {
            let (s, rest) = format(&tokens[1..]);
            match op {
                interpreter::UnaryOp::Neg => (format!("(-{})", s), rest),
                interpreter::UnaryOp::Not => (format!("(!{})", s), rest),
                interpreter::UnaryOp::ToInt => (format!("(Number({}))", s), rest),
                interpreter::UnaryOp::ToStr => (format!("(({}).toString())", s), rest),
            }
        }
        Token::Binary(op) => {
            let (s1, rest) = format(&tokens[1..]);
            let (s2, rest) = format(rest);
            match op {
                interpreter::BinaryOp::Add => (format!("({} + {})", s1, s2), rest),
                interpreter::BinaryOp::Sub => (format!("({} - {})", s1, s2), rest),
                interpreter::BinaryOp::Mul => (format!("({} * {})", s1, s2), rest),
                interpreter::BinaryOp::Div => (format!("({} / {})", s1, s2), rest),
                interpreter::BinaryOp::Mod => (format!("({} % {})", s1, s2), rest),
                interpreter::BinaryOp::LessThan => (format!("({} < {})", s1, s2), rest),
                interpreter::BinaryOp::GreaterThan => (format!("({} > {})", s1, s2), rest),
                interpreter::BinaryOp::Equal => (format!("({} == {})", s1, s2), rest),
                interpreter::BinaryOp::Or => (format!("({} || {})", s1, s2), rest),
                interpreter::BinaryOp::And => (format!("({} && {})", s1, s2), rest),
                interpreter::BinaryOp::Concat => (format!("({} + {})", s1, s2), rest),
                interpreter::BinaryOp::Take => (format!("({s2}.slice(0, {s1}))"), rest),
                interpreter::BinaryOp::Drop => (format!("({s2}.slice({s1}))"), rest),
                interpreter::BinaryOp::Lambda => (format!("({})({})", s1, s2), rest),
            }
        }
        Token::If => {
            let (s1, rest) = format(&tokens[1..]);
            let (s2, rest) = format(rest);
            let (s3, rest) = format(rest);
            (format!("(({}) ? ({}) : ({}))", s1, s2, s3), rest)
        }
        Token::Lambda(t) => {
            let (s, rest) = format(&tokens[1..]);
            (format!("((x{}) => {})", t, s), rest)
        }
        Token::Var(v) => (format!("(x{})", v), &tokens[1..]),
    }
}
