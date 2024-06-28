use crate::Token;

#[derive(Debug, Clone)]
pub struct Node {
    pub token: Token,
    pub args: Vec<Node>,
}

pub fn parse_node(tokens: &[Token]) -> (Node, &[Token]) {
    let token = tokens[0].clone();
    let tokens = &tokens[1..];
    match &token {
        Token::True | Token::False | Token::Int(_) | Token::Str(_) | Token::Var(_) => (
            Node {
                token,
                args: vec![],
            },
            tokens,
        ),
        Token::Unary(_) => {
            let (node, tokens) = parse_node(tokens);
            (
                Node {
                    token,
                    args: vec![node],
                },
                tokens,
            )
        }
        Token::Lambda(_) => {
            let (node, tokens) = parse_node(tokens);
            assert!(matches!(node.token, Token::Var(_)) || matches!(node.token, Token::Lambda(_)));
            (
                Node {
                    token,
                    args: vec![node],
                },
                tokens,
            )
        }
        Token::Binary(_) => {
            let (left, tokens) = parse_node(tokens);
            let (right, tokens) = parse_node(tokens);
            (
                Node {
                    token,
                    args: vec![left, right],
                },
                tokens,
            )
        }
        Token::If => {
            let (first, tokens) = parse_node(tokens);
            let (second, tokens) = parse_node(tokens);
            let (third, tokens) = parse_node(tokens);
            (
                Node {
                    token,
                    args: vec![first, second, third],
                },
                tokens,
            )
        }
    }
}
