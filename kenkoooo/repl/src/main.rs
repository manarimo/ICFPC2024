use std::io::stdin;

use interpreter::{encode_int, encode_str, eval::EvalResult, execute};

fn read() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

fn main() {
    loop {
        let input = read();
        let result = execute(&input);

        eprintln!("{:?}", result);
        match result {
            EvalResult::BoolValue(b) => {
                if b {
                    println!("T");
                } else {
                    println!("F");
                }
            }
            EvalResult::IntValue(i) => println!("I{}", encode_int(i)),
            EvalResult::StrValue(s) => println!("S{}", encode_str(&s)),
            EvalResult::Function { .. } => unreachable!(),
        }
    }
}
