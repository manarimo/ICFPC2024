import multiprocessing.pool
from typing import Optional, Tuple, List, Set
from dataclasses import dataclass
import math
import functools
import sys
import multiprocessing
import itertools
import random


@functools.lru_cache(maxsize=None)
def factorize(x: int) -> Set[int]:
    factors = set()
    p = 2
    while p * p <= x:
        while x % p == 0:
            factors.add(p)
            x //= p
        p += 1
    if x > 1:
        factors.add(x)
    return factors


@functools.lru_cache(maxsize=None)
def is_primitive_root(modulo: int, g: int) -> bool:
    # https://37zigen.com/primitive-root/#i-4
    return all(pow(g, (modulo - 1) // factor, modulo) != 1 for factor in factorize(modulo - 1))


def primitive_root(modulo: int) -> int:
    # primitive root always exists when modulo is prime
    if modulo == 2 ** 31 - 1:
        # wikipedia recommendation
        return 48271
    else:
        for g in range(2, modulo):
            if is_primitive_root(modulo, g):
                return g
    raise ValueError("failed to find a primitive root")


class RNG:
    def __init__(self, initial_state: int, modulo: int, coef: Optional[int] = None) -> None:
        self.state = initial_state
        self.modulo = modulo
        self._determine_coef(coef)

    def _determine_coef(self, coef: Optional[int]):
        if coef is None:
            self.coef = primitive_root(self.modulo)

        else:
            self.coef = coef

    def get_integer(self) -> int:
        ret = self.state
        self.state = self.coef * self.state % self.modulo
        return ret


@dataclass
class SimulationResult:
    steps: int
    pills: int


def simulate(problem: str, moves: str):
    field = [[c for c in row] for row in problem.strip().split('\n')]
    rows = len(field)
    cols = len(field[0])
    lambda_r, lambda_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'L':
                lambda_r, lambda_c = r, c
                field[r][c] = ' '
    pills = sum([1 for row in field for c in row if c == '.'])
    for steps, move in enumerate(moves):
        dr, dc = {
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0),
            "U": (-1, 0),
        }[move]
        nr, nc = lambda_r + dr, lambda_c + dc
        if not 0 <= nr < rows or not 0 <= nc < cols:
            continue
        if field[nr][nc] == '#':
            continue
        if field[nr][nc] == '.':
            pills -= 1
        field[nr][nc] = ' '
        lambda_r, lambda_c = nr, nc
        if pills == 0:
            break
    return SimulationResult(steps=steps + 1, pills=pills)


@dataclass
class RandomWalk:
    moves: str
    modulo: int
    seed: int
    coef: int
    terminal: int


def generate_walk(modulo: int, seed: int, max_step: int, coef: Optional[int] = None) -> RandomWalk:
    rng = RNG(seed, modulo, coef)
    moves = []

    steps = min(modulo - 2, max_step)
    for step in range(steps):
        value = rng.get_integer()
        move = "UDRL"[value % 4]
        moves.append((math.ceil(math.log(value, 94)), value, move, step))

    least_steps = int(steps * 0.9)
    _, terminal, _, terminal_index = min(moves[least_steps:], key=lambda t: (t[0], -t[3]))
    moves = [move for _, _, move, step in moves if step < terminal_index]
    return RandomWalk(
        moves=''.join(reversed(moves)),
        modulo=modulo,
        seed=seed,
        coef=rng.coef,
        terminal=terminal,
    )


def run_solution(problem: str, modulo: int, seed: int, coef: Optional[int] = None) -> Tuple[SimulationResult, RandomWalk]:
    walk = generate_walk(modulo, seed, 999950, coef)
    result = simulate(problem, walk.moves)
    return result, walk


def random_walk_icfp(config: RandomWalk, problem_id: int) -> str:
    return f"""\
-- Make recursive Solve
B$
Lf
    B$ B$ vf vf @I{config.seed}
-- Solve :: Self -> Int -> String
Ls Lp
    ? (B= vp @I{config.terminal})
    @Ssolve@_lambdaman{problem_id}@_
    B.
      B$ B$ vs vs (B% (B* @I{config.coef} vp) @I{config.modulo})
      BT @I1 BD (B% vp @I4) @SUDRL
"""


def list_primes(upper_bound: int) -> List[int]:
    table = [True] * upper_bound
    table[0] = table[1] = False
    primes = []
    for n, is_prime in enumerate(table):
        if not is_prime:
            continue
        primes.append(n)
        for composite in range(n * n, upper_bound, n):
            table[composite] = False
    return primes


@dataclass
class Problem:
    initial_state: str
    problem_id: int


def solve(problem: Problem, chunk_size: int = 100) -> Optional[str]:
    primes = [p for p in list_primes(1000000) if 94 ** 1 <= p < 94 ** 2]
    seeds = range(1, 94)
    coefs = range(2, 94)

    args = [(modulo, seed, coef) for modulo, seed, coef in itertools.product(primes, seeds, coefs) if is_primitive_root(modulo, coef)]
    random.shuffle(args)

    print(f"running {len(args)} cases", file=sys.stderr)
    with multiprocessing.Pool() as pool:
        for begin in range(0, len(args), chunk_size):
            print(f"{begin} -> {begin + chunk_size}", file=sys.stderr)
            to_map = [(problem.initial_state, ) + arg for arg in args[begin: begin + chunk_size]]
            for result, walk in pool.starmap(run_solution, to_map):
                if result.pills == 0:
                    print(f"successfully solved with the following parameters. modulo = {walk.modulo}, seed = {walk.seed}, coef = {walk.coef}, result = {result}", file=sys.stderr)
                    return random_walk_icfp(walk, problem.problem_id)
    return None


def main():
    from pathlib import Path
    problem_id = 4
    chunk_size = 10000

    repository_root = Path(__file__).absolute().parent.parent
    problem_file = repository_root / "lambdaman" / "in" / f"{problem_id:02}.txt"
    with problem_file.open() as f:
        initial_state = f.read().strip()

    problem = Problem(initial_state, problem_id)
    solution = solve(problem, chunk_size=chunk_size)
    if solution is None:
        raise ValueError("failed to solve")
    print(solution)


if __name__ == "__main__":
    main()
