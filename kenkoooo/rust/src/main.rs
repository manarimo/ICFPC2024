use std::io::stdin;

use rust::{encode_tokens, eval::evaluate, parse_token, tree::parse_node, Token};

fn read() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

fn main() {
    let input = read();
    let tokens = input
        .trim()
        .split_whitespace()
        .map(|token| parse_token(token.as_bytes()))
        .collect::<Vec<_>>();

    for token in &tokens {
        eprintln!("{:?}", token);
    }

    let (node, tokens) = parse_node(&tokens);
    eprintln!("{:#?}", node);
    assert!(tokens.is_empty());

    let result = evaluate(node);
    eprintln!("{:?}", result);
}
