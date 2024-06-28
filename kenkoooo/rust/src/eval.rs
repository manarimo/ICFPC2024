use std::collections::HashMap;

use crate::{tree::Node, BinaryOp, Token, UnaryOp};

pub fn evaluate(node: Node) -> EvalResult {
    match node.token {
        Token::True => EvalResult::BoolValue(true),
        Token::False => EvalResult::BoolValue(false),
        Token::Int(x) => EvalResult::IntValue(x),
        Token::Str(s) => EvalResult::StrValue(s),
        Token::Unary(op) => {
            assert_eq!(node.args.len(), 1);
            let arg = node.args.into_iter().next().expect("unreachable");
            let value = evaluate(arg);
            unary_op(op, value)
        }
        Token::Binary(op) => {
            assert_eq!(node.args.len(), 2);
            let left = node.args[0].clone();
            let right = node.args[1].clone();
            let left = evaluate(left);
            let right = evaluate(right);
            binary_op(op, left, right)
        }
        Token::If => {
            assert_eq!(node.args.len(), 3);
            let cond = node.args[0].clone();
            let then = node.args[1].clone();
            let els = node.args[2].clone();
            let cond = evaluate(cond);
            if let EvalResult::BoolValue(true) = cond {
                evaluate(then)
            } else {
                evaluate(els)
            }
        }
        Token::Lambda(id) => {
            let mut args = vec![id];
            let mut node = node.args[0].clone();
            loop {
                match node.token {
                    Token::Lambda(id) => {
                        args.push(id);
                        node = node.args[0].clone();
                    }
                    Token::Var(id) => {
                        return EvalResult::Function {
                            args,
                            ret: id,
                            ctx: HashMap::new(),
                        }
                    }
                    _ => unreachable!(),
                }
            }
        }
        Token::Var(_) => unreachable!(),
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum EvalResult {
    BoolValue(bool),
    IntValue(i128),
    StrValue(String),
    Function {
        args: Vec<i128>,
        ret: i128,
        ctx: HashMap<i128, EvalResult>,
    },
}

pub fn unary_op(op: UnaryOp, value: EvalResult) -> EvalResult {
    const ORDER: &str = r###"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`|~ 
    "###;
    match (op, value) {
        (UnaryOp::Neg, EvalResult::IntValue(x)) => EvalResult::IntValue(-x),
        (UnaryOp::Not, EvalResult::BoolValue(b)) => EvalResult::BoolValue(!b),
        (UnaryOp::ToInt, EvalResult::StrValue(s)) => {
            let mut value = 0;
            for c in s.chars() {
                value = value * 94 + ORDER.find(c).expect("unreachable") as i128;
            }
            EvalResult::IntValue(value)
        }
        (UnaryOp::ToStr, EvalResult::IntValue(mut x)) => {
            let mut value = String::new();
            while x > 0 {
                value.push(ORDER.chars().nth((x % 94) as usize).expect("unreachable"));
                x /= 94;
            }
            EvalResult::StrValue(value.chars().rev().collect::<String>())
        }
        _ => unreachable!(),
    }
}

pub fn binary_op(op: BinaryOp, left: EvalResult, right: EvalResult) -> EvalResult {
    match (op, left, right) {
        (BinaryOp::Add, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::IntValue(x + y)
        }
        (BinaryOp::Sub, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::IntValue(x - y)
        }
        (BinaryOp::Mul, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::IntValue(x * y)
        }
        (BinaryOp::Div, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::IntValue(x / y)
        }
        (BinaryOp::Mod, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::IntValue(x % y)
        }
        (BinaryOp::LessThan, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::BoolValue(x < y)
        }
        (BinaryOp::GreaterThan, EvalResult::IntValue(x), EvalResult::IntValue(y)) => {
            EvalResult::BoolValue(x > y)
        }
        (BinaryOp::Equal, x, y) => EvalResult::BoolValue(x == y),
        (BinaryOp::Or, EvalResult::BoolValue(x), EvalResult::BoolValue(y)) => {
            EvalResult::BoolValue(x || y)
        }
        (BinaryOp::And, EvalResult::BoolValue(x), EvalResult::BoolValue(y)) => {
            EvalResult::BoolValue(x && y)
        }
        (BinaryOp::Concat, EvalResult::StrValue(x), EvalResult::StrValue(y)) => {
            EvalResult::StrValue(x + &y)
        }
        (BinaryOp::Take, EvalResult::IntValue(x), EvalResult::StrValue(y)) => {
            EvalResult::StrValue(y.chars().take(x as usize).collect())
        }
        (BinaryOp::Drop, EvalResult::IntValue(x), EvalResult::StrValue(y)) => {
            EvalResult::StrValue(y.chars().skip(x as usize).collect())
        }
        (BinaryOp::Lambda, EvalResult::Function { args, ret, mut ctx }, y) => {
            ctx.insert(args[0], y);
            let args = args.into_iter().skip(1).collect::<Vec<_>>();
            if args.is_empty() {
                let value = ctx.remove(&ret).expect("unreachable");
                value
            } else {
                EvalResult::Function { args, ret, ctx }
            }
        }
        _ => unreachable!(),
    }
}
