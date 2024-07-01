import maze
from dataclasses import dataclass
from typing import Optional, Tuple, List
import copy

@dataclass
class Problem:
    initial_field: List[List[str]]
    initial_r: int
    initial_c: int
    num_cells: int

def load_problem(path):
    with open(path, encoding="ascii") as f:
        initial_state = f.read().strip()

    initial_field = [[c for c in row] for row in initial_state.strip().split('\n')]
    rows = len(initial_field)
    cols = len(initial_field[0])
    num_cells = 0
    for r in range(rows):
        for c in range(cols):
            if initial_field[r][c] == 'L':
                initial_r, initial_c = r, c
                initial_field[r][c] = ' '
            if initial_field[r][c] == '.':
                num_cells += 1
    return Problem(initial_field, initial_r, initial_c, num_cells)

def simulate(problem, seed, sim_len, row_range = None, col_range = None):
    rng = maze.RNG(seed, 2 ** 31 - 1)
    moves = []
    switched = False
    r, c = problem.initial_r, problem.initial_c
    rows = len(problem.initial_field)
    cols = len(problem.initial_field[0])
    field = copy.deepcopy(problem.initial_field)

    if row_range is None:
        row_range = range(rows)
    if col_range is None:
        col_range = range(cols)

    num_targets = 0
    for row in field[row_range.start:row_range.stop]:
        for col in row[col_range.start:col_range.stop]:
            if col == '.':
                num_targets += 1
    num_taken = 0
    completed_step = None
    home_steps = []

    for i in range(sim_len):
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
        if field[nr][nc] == '#':
            continue
        if field[nr][nc] == '.':
            field[nr][nc] = ' '
            if nr in row_range and nc in col_range:
                num_taken += 1
                if num_taken == num_targets:
                    completed_step = i
        if (nr, nc) == (problem.initial_r, problem.initial_c):
            home_steps.append(i)
        r, c = nr, nc

    missing = None
    if num_targets - num_taken < 10:
        missing = []
        for row in row_range:
            for col in col_range:
                if field[row][col] == '.':
                    missing.append((row, col))
    return (''.join(moves), num_taken, num_targets, completed_step, home_steps, missing)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help="problem_file")
    parser.add_argument("-i", "--problem-id", help="problem_id")

    args = parser.parse_args()
    problem = load_problem(args.problem)

    for i in range(1000, 2000):
        print(f"Testing {i}")
        code, num_taken, num_targets, completed_step, home_steps, missing = simulate(problem, 12356+i, 600000, None, range(0, 50))
        # code, num_taken, num_targets, completed_step, home_steps = simulate(problem, 12356+i, None, range(0, 159))
        if completed_step is not None:
            print('C', 12356+i, completed_step, home_steps)
            #print(code[0:208807])
        if missing is not None:
            print('M', 12356+i, missing)
        print(f"{num_taken}/{num_targets}")
    # print(code)


if __name__ == "__main__":
    main()
