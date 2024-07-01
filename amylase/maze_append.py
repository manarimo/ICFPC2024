import json
from base94 import compress
from typing import Tuple
import sys
from collections import deque


try:
    sys.setrecursionlimit(100_000)
except:
    pass


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


def get_append(simulator: Simulator, problem_id: int):
    if problem_id == 18:
        return "RRUUUUUURRRRRRRRRRRRRUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUUUUUUURUUURRRRRRRRRRRRRRRRRUUUURRDRRRRRRRRDDDDDD"
    else:
        pass

def main():
    problem_id = 20
    with open(f"best{problem_id:02}.json", encoding="ascii") as f:
        best = json.load(f)
    with open(f"../lambdaman/in/{problem_id:02}.txt") as f:
        problem = f.read().strip()
    walk_program = best["program"]
    walk_moves = best["moves"]

    simulator = Simulator(problem)
    simulator.move(walk_moves)
    append_moves = []
    while simulator.pills > 0:
        memo = {}
        q = deque()
        for r in range(simulator.rows):
            for c in range(simulator.cols):
                if simulator.field[r][c] == '.':
                    memo[(r, c)] = 0
                    q.append((r, c))
        while len(q) > 0:
            r, c = q.popleft()
            for move in "LRDU":
                dr, dc = vectors[move]
                nr, nc = r + dr, c + dc
                if not 0 <= nr < simulator.rows or not 0 <= nc < simulator.cols:
                    continue
                if simulator.field[nr][nc] == '#':
                    continue
                if (nr, nc) in memo:
                    continue
                memo[(nr, nc)] = memo[(r, c)] + 1
                q.append((nr, nc))

        best_move = 2 ** 51, "Z"
        for move in "LRDU":
            dr, dc = vectors[move]
            nr, nc = simulator.lambda_r + dr, simulator.lambda_c + dc
            if not 0 <= nr < simulator.rows or not 0 <= nc < simulator.cols:
                continue
            if simulator.field[nr][nc] == '#':
                continue
            best_move = min(best_move, (memo[(nr, nc)], move))
        append_moves.append(best_move[1])
        simulator.move(best_move[1])
        print(best_move, simulator.lambda_r, simulator.lambda_c, simulator.pills)

    append_moves = ''.join(append_moves)
    print(f"done. appended {len(append_moves)} moves.", file=sys.stderr)

    with open(f"move{problem_id:02}.txt", "w") as f:
        f.write(walk_moves.strip())
        f.write(append_moves)

    with open(f"append.asm", "w") as f:
        print("B.", file=f)
        print(walk_program, file=f)
        # print(f"@S{append_moves}", file=f)
        print(compress(append_moves, unit_size=1), file=f)

    
if __name__ == "__main__":
    main()
