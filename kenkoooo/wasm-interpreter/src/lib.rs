use interpreter::eval::EvalResult;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn from_icfp(program: &str) -> String {
    let result = interpreter::execute(program);
    match result {
        EvalResult::BoolValue(b) => {
            if b {
                "true".to_string()
            } else {
                "false".to_string()
            }
        }
        EvalResult::IntValue(i) => i.to_string(),
        EvalResult::StrValue(s) => s,
        EvalResult::Function { .. } => unreachable!(),
    }
}
