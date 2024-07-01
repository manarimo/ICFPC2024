import io
import copy
from typing import Optional, Tuple, List
import multiprocessing
import sys


modulo = 2**31 - 1   # prime
# modulo = [999763, 999769, 999773, 999809, 999853, 999863, 999883, 999907, 999917, 999931, 999953, 999959, 999961, 999979, 999983][-1]    # prime less than 1M
# modulo = [830449, 830477, 830483, 830497, 830503, 830513, 830549, 830551, 830561, 830567, 830579][-4]    # prime less than 94 ** 3 = 830584
# modulo = 499711    # prime less than 500k


def determine_coef():
    # find a generator of F_modulo
    if modulo == 2 ** 31 - 1:
        # wikipedia recommendation
        return 48271
    for g in range(2, modulo):
        if len(set(pow(g, i, modulo) for i in range(modulo))) == modulo - 1:
            print(f"using {g} as a generator", file=sys.stderr)
            return g
    raise ValueError("failed to find a generator")


coef = determine_coef()

steps = min(modulo, 999900) - 10000


class RNG:
    def __init__(self, initial_state: int) -> None:
        self.state = initial_state

    def get_integer(self) -> int:
        ret = self.state
        self.state = coef * self.state % modulo
        return ret


# nth: 0-indexed
def nth_rand(seed: int, nth: int) -> int:
    rng = RNG(seed)
    last = seed
    for _ in range(0, nth):
        last = rng.get_integer()
    return last

def random_walk_icfp(problem_id: int, seed: int, terminal: int) -> str:
    return f"""\
-- Make recursive Solve
B$
Lf
    B$ B$ vf vf @I{seed}
-- Solve :: Self -> Int -> String
Ls Lp
    ? (B= vp @I{terminal})
    @Ssolve@_lambdaman{problem_id}@_
    B.
      B$ B$ vs vs (B% (B* @I{coef} vp) @I{modulo})
      BT @I1 BD (B% vp @I4) @SUDRL
"""


def random_walk(seed: int, length: int) -> Tuple[str, int]:
    rng = RNG(seed)
    moves = []
    switched = False
    r, c = initial_r, initial_c
    rows = len(initial_field)
    cols = len(initial_field[0])
    for i in range(length):
        d = "UDRL"[rng.get_integer() % 4]
        moves.append(d)
        dr, dc = {
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0),
            "U": (-1, 0),
        }[d]
        nr, nc = r + dr, c + dc
        if not 0 <= nr < rows or not 0 <= nc < cols:
            continue
        if initial_field[nr][nc] == '#':
            continue
        r, c = nr, nc
        #if not switched and (r, c) == (initial_r, initial_c) and i > 440000:
        #    rng = RNG(114514)
        #    switched = True

    terminal_candidates = []
    for i in range(length, min(modulo - 10, 999900)):
        v = rng.get_integer()
        d = "UDRL"[v % 4]
        moves.append(d)
        terminal_candidates.append((v, i))
    terminal, terminal_index = min(terminal_candidates)
    return ''.join(reversed(moves[:terminal_index])), terminal


initial_field = None
initial_r, initial_c = -1, -1
num_cells = 0

def simulate(seed: int) -> Tuple[List[str], Optional[int], int, int, int, List[int]]:
    if initial_field is None:
        return False
    rows = len(initial_field)
    cols = len(initial_field[0])
    field, r, c = copy.deepcopy(initial_field), initial_r, initial_c
    moves, terminal = random_walk(seed, steps)
    num_target_cells = sum([1 for row in initial_field for c in row[0:159] if c == '.'])
    num_filled_cells = 0
    completed_step = None
    home_steps = []
    for (i, move) in enumerate(moves):
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
        if field[nr][nc] == '.':
            field[nr][nc] = ' '
            num_filled_cells += 1
            if num_filled_cells == num_target_cells:
                completed_step = i
        r, c = nr, nc
        if (r, c) == (initial_r, initial_c):
            home_steps.append(i)

    visited_cells = sum([1 for row in field for c in row[0:159] if c == ' '])
    if not any(any(c == '.' for c in row) for row in field):
        return (moves, terminal, num_target_cells, visited_cells, completed_step, home_steps)
    else:
        return (moves, None, num_target_cells, visited_cells, completed_step, home_steps)

def solve_single(seed: int) -> Optional[int]:
    _, terminal, _, _ = simulate(seed)
    return terminal
    

def init_global(problem: str, problem_id: int):
    global initial_field, initial_r, initial_c, num_cells

    initial_field = [[c for c in row] for row in problem.strip().split('\n')]
    rows = len(initial_field)
    cols = len(initial_field[0])
    for r in range(rows):
        for c in range(cols):
            if initial_field[r][c] == 'L':
                initial_r, initial_c = r, c
                initial_field[r][c] = ' '
    num_cells = sum([1 for row in initial_field for c in row if c == '.'])

def solve_parallel(problem_id: int) -> Optional[str]:
    try:
        pool = multiprocessing.Pool()

        batch_size = 300
        for begin in range(0, 1000000, batch_size):
            print(f"{begin} -> {begin + batch_size}", file=sys.stderr)
            seeds = list(range(begin, begin + batch_size))
            res = pool.map(solve_single, seeds)
            for seed, terminal in zip(seeds, res):
                if terminal is not None:
                    return random_walk_icfp(problem_id, seed, terminal)
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

    init_global(problem, args.problem_id)
    code = solve_parallel(args.problem_id)
    if code is None:
        raise ValueError("failed to solve.")
    print(code)


if __name__ == "__main__":
    main()
