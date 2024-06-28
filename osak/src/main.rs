use std::{collections::HashMap, io, panic::resume_unwind};

const ALPHABETS: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n";

fn parse_icfp_int(s: &str) -> i64 {
    let mut n = 0i64;
    for c in s.bytes() {
        n *= 94;
        n += (c as i64) - 33;
    }
    return n;
}

fn to_icfp_string(n: i64) -> String {
    let mut buf = vec![];
    let mut cur = n;
    while cur > 0 {
        let m = cur % 94;
        buf.push(char::from_u32(33 + m as u32).unwrap());
        cur /= 94;
    }
    return buf.into_iter().rev().collect::<String>();
}

fn to_human_string(s: &str) -> String {
    s.chars()
        .map(|c| ALPHABETS.chars().nth((c as usize) - 33).unwrap())
        .collect::<String>()
}

#[derive(Clone, Debug, PartialEq, Eq)]
struct Node {
    pos: usize,
    token: String,
    operands: Vec<Node>,
    binding: HashMap<char, Node>,
}

impl Node {
    fn new(pos: usize, token: &str) -> Node {
        Node {
            pos,
            token: token.to_owned(),
            operands: vec![],
            binding: HashMap::new(),
        }
    }

    fn new2(pos: usize, token: &str, operands: Vec<Node>) -> Node {
        Node {
            pos,
            token: token.to_owned(),
            operands,
            binding: HashMap::new(),
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
enum Value {
    Null,
    Number(i64),
    String(String),
    Bool(bool),
    Lambda(char, Node, HashMap<char, Node>),
}

struct Program {
    tokens: Vec<String>,
    register: Vec<Value>,
    cur: usize,
    depth: usize,
}

struct Parser {
    tokens: Vec<String>,
    cur: usize,
    alpha: usize,
    mapping: HashMap<u8, usize>,
}

impl Parser {
    fn parse(&mut self) -> Node {
        let token = self.tokens[self.cur].clone();
        let bs = token.as_bytes();

        match bs[0] {
            b'T' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new(cur, &token)
            }
            b'F' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new(cur, &token)
            }
            b'I' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new(cur, &token)
            }
            b'S' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new(cur, &token)
            }
            b'U' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new2(cur, &token, vec![self.parse()])
            }
            b'B' => {
                let cur = self.cur;
                self.cur += 1;
                let opr1 = self.parse();
                let opr2 = self.parse();
                Node::new2(cur, &token, vec![opr1, opr2])
            }
            b'?' => {
                let cur = self.cur;
                self.cur += 1;
                let cond = self.parse();
                let t = self.parse();
                let f = self.parse();
                Node::new2(cur, &token, vec![cond, t, f])
            }
            b'L' => {
                let cur = self.cur;
                self.cur += 1;
                self.alpha += 1;
                let result = Node::new2(cur, &token, vec![self.parse()]);
                result
            }
            b'v' => {
                let cur = self.cur;
                self.cur += 1;
                Node::new(cur, &token)
            }
            _ => panic!("Unknown token {}", token),
        }
    }
}

/*
impl Program {
    fn evaluate(&mut self) -> Value {
        let token = &self.tokens[self.cur].clone();
        let tok_chars = token.as_bytes();
        println!("{}{} {}", "  ".repeat(self.depth), self.cur, token);
        self.depth += 1;

        let result = match tok_chars[0] {
            b'B' => {
                self.cur += 1;
                let lhs = self.evaluate();
                match tok_chars[1] {
                    b'$' => {
                        let thunk = Value::Thunk(self.cur, self.register.clone());
                        self.skip_term();
                        let cur = self.cur;
                        println!("{}app {:?} {:?}", "  ".repeat(self.depth), lhs, thunk);
                        let (lambda_ptr, reg, regs) = lhs.as_lambda_ptr(self);
                        self.cur = lambda_ptr;
                        let org_regs = self.register.clone();
                        self.register = regs.clone();
                        self.register[reg] = thunk;
                        let maybe_thunk = self.evaluate();
                        let result = self.evaluate_thunk(&maybe_thunk);
                        self.register = org_regs;
                        self.cur = cur;
                        result
                    }
                    _ => {
                        let rhs = self.evaluate();
                        match tok_chars[1] {
                            b'+' => Value::Number(lhs.as_number(self) + rhs.as_number(self)),
                            b'-' => Value::Number(lhs.as_number(self) - rhs.as_number(self)),
                            b'*' => Value::Number(lhs.as_number(self) * rhs.as_number(self)),
                            b'/' => Value::Number(lhs.as_number(self) / rhs.as_number(self)),
                            b'%' => Value::Number(lhs.as_number(self) % rhs.as_number(self)),
                            b'<' => Value::Bool(lhs.as_number(self) < rhs.as_number(self)),
                            b'>' => Value::Bool(lhs.as_number(self) > rhs.as_number(self)),
                            b'=' => Value::Bool(lhs == rhs),
                            b'|' => Value::Bool(lhs.as_bool(self) || rhs.as_bool(self)),
                            b'&' => Value::Bool(lhs.as_bool(self) && rhs.as_bool(self)),
                            b'.' => Value::String(lhs.as_string(self) + &rhs.as_string(self)),
                            b'T' => Value::String(rhs.as_string(self)[0..(lhs.as_number(self) as usize)].to_owned()),
                            b'D' => Value::String(rhs.as_string(self)[lhs.as_number(self) as usize..].to_owned()),
                            _ => panic!("Unknown binary operation {}", token),
                        }
                    }
                }
            },
            b'T' => {
                self.cur += 1;
                Value::Bool(true)
            },
            b'F' => {
                self.cur += 1;
                Value::Bool(false)
            },
            b'S' => {
                let str = &self.tokens[self.cur][1..];
                self.cur += 1;
                Value::String(str.to_owned())
            },
            b'I' => {
                let value = parse_icfp_int(&self.tokens[self.cur][1..]);
                self.cur += 1;
                Value::Number(value)
            },
            b'U' => {
                self.cur += 1;
                let opr = self.evaluate();
                match tok_chars[1] {
                    b'-' => Value::Number(-opr.as_number(self)),
                    b'!' => Value::Bool(!opr.as_bool(self)),
                    b'#' => Value::Number(parse_icfp_int(&opr.as_string(self))),
                    b'$' => Value::String(to_icfp_string(opr.as_number(self))),
                    _ => panic!("Unknown unary operation {}", token),
                }
            },
            b'?' => {
                self.cur += 1;
                let cond = self.evaluate();
                if cond.as_bool(self) {
                    self.evaluate()
                } else {
                    self.skip_term();
                    self.evaluate()
                }
            },
            b'L' => {
                let reg = parse_icfp_int(&self.tokens[self.cur][1..]);
                self.cur += 1;
                let lambda = Value::Lambda(self.cur, reg as usize, self.register.clone());
                self.skip_term();
                println!("{}next {}", "  ".repeat(self.depth), self.cur);
                lambda
            }
            b'v' => {
                let reg = parse_icfp_int(&self.tokens[self.cur][1..]);
                self.cur += 1;
                self.register[reg as usize].clone()
            }
            _ => panic!("Unknown token {}", token),
        };
        self.depth -= 1;
        println!("{}end {}", "  ".repeat(self.depth), token);
        result
    }

    fn evaluate_thunk(&mut self, thunk: &Value) -> Value {
        match thunk {
            Value::Thunk(c, reg) => {
                let org_cur = self.cur;
                let org_reg = self.register.clone();
                self.cur = *c;
                self.register = reg.clone();
                let res = self.evaluate();
                self.cur = org_cur;
                self.register = org_reg;
                match res {
                    Value::Thunk(..) => self.evaluate_thunk(&res),
                    _ => res
                }
            }
            _ => thunk.clone(),
        }
    }
}
*/

fn alpha_transform(node: &mut Node, var: char, to: char) {
    for i in 0..node.operands.len() {
        alpha_transform(&mut node.operands[i], var, to);
    }

    let token = node.token.clone();
    let bs: Vec<char> = token.chars().collect();
    if bs[0] == 'v' && bs[1] == var {
        node.token = format!("v{}", to);
    }
}

fn evaluate(node: &Node, binding: &HashMap<char, Node>) -> Value {
    if !node.binding.is_empty() && node.binding != *binding {
        return evaluate(node, &node.binding);
    }
    let token = node.token.clone();
    let bs: Vec<char> = token.chars().collect();

    println!("{} {}", node.pos, token);
    match bs[0] {
        'T' => Value::Bool(true),
        'F' => Value::Bool(false),
        'I' => Value::Number(parse_icfp_int(&token[1..])),
        'S' => Value::String(token[1..].to_string()),
        'U' => match bs[1] {
            '-' => {
                let opr = evaluate(&node.operands[0], binding);
                match opr {
                    Value::Number(n) => Value::Number(-n),
                    _ => panic!("expected number but got {:?}", opr),
                }
            }
            '!' => {
                let opr = evaluate(&node.operands[0], binding);
                match opr {
                    Value::Bool(b) => Value::Bool(!b),
                    _ => panic!("expected bool but got {:?}", opr),
                }
            }
            '#' => {
                let opr = evaluate(&node.operands[0], binding);
                match opr {
                    Value::String(s) => Value::Number(parse_icfp_int(&s)),
                    _ => panic!("expected string but got {:?}", opr),
                }
            }
            '$' => {
                let opr = evaluate(&node.operands[0], binding);
                match opr {
                    Value::Number(n) => Value::String(to_icfp_string(n)),
                    _ => panic!("expected number but got {:?}", opr),
                }
            }
            _ => panic!("Unknown node {:?}", node),
        },
        'B' => match bs[1] {
            '+' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Number(op1.as_number() + op2.as_number())
            }
            '-' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Number(op1.as_number() - op2.as_number())
            }
            '*' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Number(op1.as_number() * op2.as_number())
            }
            '/' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Number(op1.as_number() / op2.as_number())
            }
            '%' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Number(op1.as_number() % op2.as_number())
            }
            '<' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Bool(op1.as_number() < op2.as_number())
            }
            '>' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Bool(op1.as_number() > op2.as_number())
            }
            '=' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Bool(op1 == op2)
            }
            '|' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Bool(op1.as_bool() || op2.as_bool())
            }
            '&' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::Bool(op1.as_bool() && op2.as_bool())
            }
            '.' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::String(op1.as_string() + &op2.as_string())
            }
            'T' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::String(op2.as_string()[0..op1.as_number() as usize].to_string())
            }
            'D' => {
                let op1 = evaluate(&node.operands[0], binding);
                let op2 = evaluate(&node.operands[1], binding);
                Value::String(op2.as_string()[op1.as_number() as usize..].to_string())
            }
            '$' => {
                let (var, lambda_body, b) = match evaluate(&node.operands[0], binding) {
                    Value::Lambda(v, n, b) => (v, n, b),
                    _ => panic!("expected lambda {:?} {:?}", node.operands[0], binding),
                };
                let mut bound = node.operands[1].clone();
                bound.binding = binding.clone();
                let mut new_binding = b.clone();
                new_binding.insert(var, bound);
                evaluate(&lambda_body, &new_binding)
            }
            _ => panic!("unknown node {:?}", node),
        },
        '?' => {
            let cond = evaluate(&node.operands[0], binding);
            if cond.as_bool() {
                evaluate(&node.operands[1], binding)
            } else {
                evaluate(&node.operands[2], binding)
            }
        }
        'L' => {
            let var = node.token.chars().nth(1).unwrap();
            let body = node.operands[0].clone();
            Value::Lambda(var, body, binding.clone())
        }
        'v' => {
            let var = node.token.chars().nth(1).unwrap();
            evaluate(&binding[&var], binding)
        }
        _ => panic!("Unknown node {:?}", node),
    }
}

impl Value {
    fn as_number(&self) -> i64 {
        match self {
            Value::Number(i) => *i,
            _ => panic!("not a number: {:?}", self),
        }
    }

    fn as_bool(&self) -> bool {
        match self {
            Value::Bool(b) => *b,
            _ => panic!("not a bool"),
        }
    }

    fn as_string(&self) -> String {
        match self {
            Value::String(s) => s.to_string(),
            _ => panic!("not a string"),
        }
    }
}

fn main() {
    // let code = "B$ B$ L\" B$ L# B$ v\" B$ v# v# L# B$ v\" B$ v# v# L\" L# ? B= v# I! I\" B$ L$ B+ B$ v\" v$ B$ v\" v$ B- v# I\" I%";
    let mut code = String::new();
    io::stdin().read_line(&mut code);

    let mut parser = Parser {
        tokens: code
            .strip_suffix("\n")
            .unwrap()
            .split(' ')
            .map(|s| s.to_owned())
            .collect(),
        cur: 0,
        alpha: 0,
        mapping: HashMap::new(),
    };

    let root = parser.parse();
    let result = evaluate(&root, &HashMap::new());
    println!("{:?}", result);

    match result {
        Value::String(s) => println!("{}", to_human_string(&s)),
        _ => {}
    }
}
