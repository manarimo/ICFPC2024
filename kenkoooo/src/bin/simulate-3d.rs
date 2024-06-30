use std::collections::BTreeMap;

const W: usize = 3;

fn main() {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());

    let debug = std::env::var("3D_DEBUG").is_ok();

    let h: usize = sc.read();
    let w: usize = sc.read();

    let a: i64 = sc.read();
    let b: i64 = sc.read();

    let mut board = vec![vec![".".to_string(); w + W * 2]; h + W * 2];
    let mut submit = (0, 0);
    for i in 0..h {
        for j in 0..w {
            let c: String = sc.read();

            if c == "A" {
                board[i + W][j + W] = a.to_string();
            } else if c == "B" {
                board[i + W][j + W] = b.to_string();
            } else if c == "S" {
                submit = (i + W, j + W);
                board[i + W][j + W] = ".".to_string();
            } else {
                board[i + W][j + W] = c;
            }
        }
    }

    let mut histories = vec![board];
    let mut tick = 1;
    let mut min_area = calc_used_area(&histories[0], submit);
    while tick < 100_000 {
        let board = &histories[tick - 1];
        let next = tick_board(board);
        if next[submit.0][submit.1] != "." {
            println!(
                "submit={} tick={} area={} score={}",
                next[submit.0][submit.1],
                tick,
                min_area,
                min_area * tick
            );
            break;
        }

        match capture_warp(board) {
            Some((dt, write)) => {
                assert!(dt > 0);
                assert!(tick > dt as usize);
                tick -= dt as usize;
                histories.truncate(tick);
                for ((i, j), value) in write {
                    histories[tick - 1][i][j] = value.to_string();
                }
            }
            None => {
                histories.push(next);
                tick += 1;
            }
        }

        let area = calc_used_area(&histories[tick - 1], submit);
        min_area = min_area.max(area);
        if debug {
            println!("tick: {}", tick);
            print_board(&histories[tick - 1]);
        }
    }
}

fn calc_used_area(board: &Vec<Vec<String>>, submit: (usize, usize)) -> usize {
    let h = board.len();
    let w = board[0].len();

    let mut min_i = submit.0;
    let mut max_i = submit.0;
    let mut min_j = submit.1;
    let mut max_j = submit.1;
    for i in 0..h {
        for j in 0..w {
            if board[i][j] != "." {
                min_i = min_i.min(i);
                max_i = max_i.max(i);
                min_j = min_j.min(j);
                max_j = max_j.max(j);
            }
        }
    }

    let area = (max_i - min_i + 1) * (max_j - min_j + 1);
    area
}

fn capture_warp(board: &Vec<Vec<String>>) -> Option<(i64, BTreeMap<(usize, usize), i64>)> {
    let h = board.len();
    let w = board[0].len();

    let mut warps = BTreeMap::new();

    for i in 0..h {
        for j in 0..w {
            if board[i][j] == "@" {
                let u = board[i - 1][j].parse::<i64>();
                let l = board[i][j - 1].parse::<i64>();
                let r = board[i][j + 1].parse::<i64>();
                let d = board[i + 1][j].parse::<i64>();
                if let (Ok(u), Ok(l), Ok(r), Ok(d)) = (u, l, r, d) {
                    let value = u;
                    let dt = d;
                    let dx = l;
                    let dy = r;

                    let i = (i as i64 - dy) as usize;
                    let j = (j as i64 - dx) as usize;

                    warps.entry(dt).or_insert_with(Vec::new).push((i, j, value));
                }
            }
        }
    }

    assert!(warps.len() <= 1, "{:?}", warps);
    let (dt, warps) = warps.into_iter().next()?;
    let mut write = BTreeMap::new();
    for (i, j, value) in warps {
        let cur = write.entry((i, j)).or_insert(value);
        assert_eq!(*cur, value);
    }

    Some((dt, write))
}

fn tick_board(board: &Vec<Vec<String>>) -> Vec<Vec<String>> {
    let h = board.len();
    let w = board[0].len();

    let mut next = vec![vec![".".to_string(); w]; h];
    let mut moved = vec![vec![false; w]; h];

    for i in 0..h {
        for j in 0..w {
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
                "@" => {
                    // do nothing
                }
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
            if !moved[i][j] && board[i][j] != "." && next[i][j] == "." {
                next[i][j] = board[i][j].clone();
            }
        }
    }

    next
}

fn print_board(board: &Vec<Vec<String>>) {
    let w = board[0].len();
    let lengths = (0..w)
        .map(|j| board.iter().map(|row| row[j].len()).max().unwrap_or(0))
        .collect::<Vec<_>>();

    for row in board.iter() {
        for (cell, length) in row.iter().zip(lengths.iter()) {
            let spaces = length - cell.len() + 1;
            let spaces = " ".repeat(spaces);
            print!("{}{}", spaces, cell);
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
