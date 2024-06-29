fn main() {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());

    let h: usize = sc.read();
    let w: usize = sc.read();

    let a: i64 = sc.read();
    let b: i64 = sc.read();

    let mut board = vec![vec![".".to_string(); w + 2]; h + 2];
    for i in 0..h {
        for j in 0..w {
            let c: String = sc.read();

            if c == "A" {
                board[i + 1][j + 1] = a.to_string();
            } else if c == "B" {
                board[i + 1][j + 1] = b.to_string();
            } else {
                board[i + 1][j + 1] = c;
            }
        }
    }

    let w = w + 2;
    let h = h + 2;

    let mut histories = vec![board];
    for t in 1..=30 {
        let board = &histories[t - 1];
        let mut next = vec![vec![".".to_string(); w]; h];
        let mut moved = vec![vec![false; w]; h];

        for i in 1..(h - 1) {
            for j in 1..(w - 1) {
                match board[i][j].as_str() {
                    ">" => {
                        if board[i][j - 1] != "." {
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = board[i][j - 1].clone();
                            moved[i][j - 1] = true;
                        }
                    }
                    "<" => {
                        if board[i][j + 1] != "." {
                            assert_eq!(next[i][j - 1], ".");
                            next[i][j - 1] = board[i][j + 1].clone();
                            moved[i][j + 1] = true;
                        }
                    }
                    "^" => {
                        if board[i + 1][j] != "." {
                            assert_eq!(next[i - 1][j], ".");
                            next[i - 1][j] = board[i + 1][j].clone();
                            moved[i + 1][j] = true;
                        }
                    }
                    "v" => {
                        if board[i - 1][j] != "." {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = board[i - 1][j].clone();
                            moved[i - 1][j] = true;
                        }
                    }
                    "+" => {
                        let u = board[i - 1][j].parse::<i64>();
                        let l = board[i][j - 1].parse::<i64>();
                        if let (Ok(u), Ok(l)) = (u, l) {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = (u + l).to_string();
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = (u + l).to_string();

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "-" => {
                        let u = board[i - 1][j].parse::<i64>();
                        let l = board[i][j - 1].parse::<i64>();
                        if let (Ok(u), Ok(l)) = (u, l) {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = (l - u).to_string();
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = (l - u).to_string();

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "*" => {
                        let u = board[i - 1][j].parse::<i64>();
                        let l = board[i][j - 1].parse::<i64>();
                        if let (Ok(u), Ok(l)) = (u, l) {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = (u * l).to_string();
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = (u * l).to_string();

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "/" => {
                        let u = board[i - 1][j].parse::<i64>();
                        let l = board[i][j - 1].parse::<i64>();
                        if let (Ok(u), Ok(l)) = (u, l) {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = (l / u).to_string();
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = (l / u).to_string();

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "%" => {
                        let u = board[i - 1][j].parse::<i64>();
                        let l = board[i][j - 1].parse::<i64>();
                        if let (Ok(u), Ok(l)) = (u, l) {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = (l % u).to_string();
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = (l % u).to_string();

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "@" => {}
                    "=" => {
                        let u = board[i - 1][j].clone();
                        let l = board[i][j - 1].clone();
                        if u == l && u != "." && l != "." {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = u;
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = l;

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    "#" => {
                        let u = board[i - 1][j].clone();
                        let l = board[i][j - 1].clone();
                        if u != l && u != "." && l != "." {
                            assert_eq!(next[i + 1][j], ".");
                            next[i + 1][j] = u;
                            assert_eq!(next[i][j + 1], ".");
                            next[i][j + 1] = l;

                            moved[i - 1][j] = true;
                            moved[i][j - 1] = true;
                        }
                    }
                    _ => {}
                }
            }
        }

        for i in 0..h {
            for j in 0..w {
                if board[i][j] == "S" {
                    if next[i][j] != "." {
                        println!("{}", next[i][j]);
                        return;
                    } else {
                        next[i][j] = "S".to_string();
                    }
                } else if !moved[i][j] && board[i][j] != "." {
                    assert_eq!(next[i][j], ".");
                    next[i][j] = board[i][j].clone();
                }
            }
        }

        histories.push(next);
        print_board(&histories[t]);
    }
}

fn print_board(board: &Vec<Vec<String>>) {
    for row in board.iter() {
        for cell in row.iter() {
            print!("{} ", cell);
        }
        println!();
    }
    println!();
}

pub struct IO<R, W: std::io::Write>(R, std::io::BufWriter<W>);

impl<R: std::io::Read, W: std::io::Write> IO<R, W> {
    pub fn new(r: R, w: W) -> Self {
        Self(r, std::io::BufWriter::new(w))
    }
    pub fn write<S: ToString>(&mut self, s: S) {
        use std::io::Write;
        self.1.write_all(s.to_string().as_bytes()).unwrap();
    }
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .0
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n' || b == b'\r' || b == b'\t')
            .take_while(|&b| b != b' ' && b != b'\n' && b != b'\r' && b != b'\t')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
            .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn usize0(&mut self) -> usize {
        self.read::<usize>() - 1
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}
