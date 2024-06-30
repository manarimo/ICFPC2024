import io
import copy
from typing import Optional
import multiprocessing
import sys


def random_walk_icfp(seed: int, length: int) -> str:
    return f"""\
B$
Lf
    B$ B$ B$ vf vf @I{length} @I{seed}
-- Solve :: Self -> Int -> Int -> String
Ls Ln Lp
    ? (B= vn @I0)
    S
    B$ L1 -- rand1
      B.
        BT @I1 BD (B% v1 @I4) @SUDRL
        B$ B$ B$ vs vs (B- vn @I1) v1
    B% (B* @I48271 vp) @I78074891
"""


class RNG:
    def __init__(self, initial_state: int) -> None:
        self.state = initial_state
    
    def get_integer(self) -> int:
        self.state = 48271 * self.state % ((2 ** 31) - 1)
        return self.state


def random_walk(seed: int, length: int) -> str:
    rng = RNG(seed)
    buf = io.StringIO()
    for _ in range(length):
        d = "UDRL"[rng.get_integer() % 4]
        buf.write(d)
    return buf.getvalue()


steps = 999000

initial_field = None
initial_r, initial_c = -1, -1


def solve_single(seed: int) -> bool:
    if initial_field is None:
        return False
    rows = len(initial_field)
    cols = len(initial_field[0])
    field, r, c = copy.deepcopy(initial_field), initial_r, initial_c
    for move in random_walk(seed, steps):
        dr, dc = {
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0),
            "U": (-1, 0),
        }[move]
        nr, nc = r + dr, c + dc
        if not 0 <= nr < rows or not 0 <= nc < cols:
            continue
        if field[nr][nc] == '#':
            continue
        field[nr][nc] = ' '
        r, c = nr, nc
    return not any(any(c == '.' for c in row) for row in field)


def solve(problem: str) -> Optional[str]:
    global initial_field, initial_r, initial_c

    initial_field = [[c for c in row] for row in problem.strip().split('\n')]
    rows = len(initial_field)
    cols = len(initial_field[0])
    for r in range(rows):
        for c in range(cols):
            if initial_field[r][c] == 'L':
                initial_r, initial_c = r, c
                initial_field[r][c] = ' '

    try:
        pool = multiprocessing.Pool()

        batch_size = 300
        for begin in range(0, 100000, batch_size):
            print(f"{begin} -> {begin + batch_size}", file=sys.stderr)
            seeds = list(range(begin, begin + batch_size))
            res = pool.map(solve_single, seeds)
            for seed, ok in zip(seeds, res):
                if ok:
                    return random_walk_icfp(seed, steps)
    finally:
        pool.close()

    return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help="problem_file")
    parser.add_argument("-i", "--problem-id", help="problem_id")

    args = parser.parse_args()
    with open(args.problem, encoding="ascii") as f:
        problem = f.read()

    body_code = solve(problem)
    if body_code is None:
        raise ValueError("failed to solve.")
    print(f"B. @Ssolve@_lambdaman{args.problem_id}@_")
    print(body_code)


if __name__ == "__main__":
    main()
