import json
from typing import Tuple
from maze_search import RNG
import re


class Simulator:
    def __init__(self, problem: str) -> None:
        self.field = [[c for c in row] for row in problem.strip().split('\n')]
        self.lambda_r, self.lambda_c = -1, -1
        for r in range(self.rows):
            for c in range(self.cols):
                if self.field[r][c] == 'L':
                    self.lambda_r, self.lambda_c = r, c
                    self.field[r][c] = ' '
        self.pills = sum([1 for row in self.field for c in row if c == '.'])
        self.tick = 0

    def move(self, moves: str) -> None:
        for move in moves:
            self.tick += 1
            dr, dc = {
                "L": (0, -1),
                "R": (0, 1),
                "D": (1, 0),
                "U": (-1, 0),
            }[move]
            nr, nc = self.lambda_r + dr, self.lambda_c + dc
            if not 0 <= nr < self.rows or not 0 <= nc < self.cols:
                continue
            if self.field[nr][nc] == '#':
                continue
            if self.field[nr][nc] == '.':
                self.pills -= 1
            self.field[nr][nc] = ' '
            self.lambda_r, self.lambda_c = nr, nc
        
    @property
    def rows(self):
        return len(self.field)
    
    @property
    def cols(self):
        return len(self.field[0])


P = Tuple[int, int]
vectors = { "L": (0, -1), "R": (0, 1), "D": (1, 0), "U": (-1, 0), }


def extract_params(program: str):
    keys = {0: "seed", 1: "terminal", 2: "coef", 3: "modulo", 4: "step_size"}
    params = {}
    for i, match in enumerate(re.findall(r"@I(\d+)", program)):
        if i in keys:
            params[keys[i]] = int(match)
    return params


def main():
    problem_id = 20
    with open(f"best{problem_id:02}.json", encoding="ascii") as f:
        best = json.load(f)
    with open(f"../lambdaman/in/{problem_id:02}.txt") as f:
        problem = f.read().strip()
    walk_program = best["program"]
    walk_moves = best["moves"]
    params = extract_params(walk_program)

    rng = RNG(params["seed"], params["modulo"], params["coef"])
    states = []
    while True:
        value = rng.get_integer()
        if value == params["terminal"]:
            break
        move = "UDRL"[value % 4] * params["step_size"]
        states.append((value, move))

    states.reverse()
    reconstructed_moves = ''.join([move for value, move in states])
    assert walk_moves == reconstructed_moves

    walk_simulator = Simulator(problem)
    walk_simulator.move(walk_moves)
    
    entry_points = set()
    for r in range(walk_simulator.rows):
        for c in range(walk_simulator.cols):
            if walk_simulator.field[r][c] != '.':
                continue
            for direction in "UDRL":
                dr, dc = vectors[direction]
                nr, nc = r + dr, c + dc
                if not 0 <= nr < walk_simulator.rows or not 0 <= nc < walk_simulator.cols:
                    continue
                if walk_simulator.field[nr][nc] == '#':
                    continue
                if walk_simulator.field[nr][nc] == ' ':
                    entry_points.add((nr, nc))

    print(f"found {len(entry_points)} entry points")
    print(entry_points)

    simulator = Simulator(problem)
    for value, move in states:
        pos = simulator.lambda_r, simulator.lambda_c
        if pos in entry_points:
            print(value, pos)
            entry_points.remove(pos)
        simulator.move(move)
    assert len(entry_points) == 0

    print(walk_program)
    with open("appendmove.txt", "w") as f:
        f.write(walk_moves)


if __name__ == "__main__":
    main()
