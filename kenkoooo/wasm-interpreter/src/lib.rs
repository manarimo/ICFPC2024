use interpreter::{encode_int, encode_str, eval::EvalResult};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn interpret(program: &str) -> String {
    let result = interpreter::execute(program);
    match result {
        EvalResult::BoolValue(b) => {
            if b {
                "T".to_string()
            } else {
                "F".to_string()
            }
        }
        EvalResult::IntValue(i) => format!("I{}", encode_int(i)),
        EvalResult::StrValue(s) => format!("S{}", encode_str(&s)),
        EvalResult::Function { .. } => unreachable!(),
    }
}
