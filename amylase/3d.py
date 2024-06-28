from argparse import ArgumentParser
from typing import List, Tuple, Dict, Union
import re
from collections import defaultdict
import io


Coordinate = Tuple[int, int]
Element = Union[int, str]

OPERATORS = "<>^v+-*/%@=#SAB"


class Board:
    operators: Dict[Coordinate, Element]

    def __init__(self, operators: Dict[Coordinate, Element]) -> None:
        self.operators = operators

    @property
    def min_x(self) -> int:
        return min(x for x, y in self.operators.keys())

    @property
    def max_x(self) -> int:
        return max(x for x, y in self.operators.keys())

    @property
    def min_y(self) -> int:
        return min(y for x, y in self.operators.keys())

    @property
    def max_y(self) -> int:
        return max(y for x, y in self.operators.keys())
    
    def substitute(self, operator: str, value: int):
        for coordinate in self.operators.keys():
            if self[coordinate] == operator:
                self.operators[coordinate] = value

    @property
    def submission_places(self) -> List[Coordinate]:
        return [c for c, v in self.operators.items() if v == "S"]
    
    def __getitem__(self, key: Coordinate) -> Element:
        return self.operators.get(key, ".")
    
    def __str__(self) -> str:
        buf = io.StringIO()
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                buf.write(str(self[x, y]))
                buf.write(" ")
            buf.write("\n")
        return buf.getvalue()


def parse_board(source_code: str) -> Board:
    operators = {}
    for x, line in enumerate(source_code.splitlines()):
        for y, token in enumerate(re.split(r"\s+", line)):
            if token == ".":
                continue
            elif token in OPERATORS:
                operators[x, y] = token
            else:
                value = int(token)
                if not -99 <= value <= 99:
                    raise ValueError("integer value must be within [-99, 99] in the source code")
                operators[x, y] = value
    return Board(operators)


def run(source_code: str, a: int, b: int, verbose: bool = False):
    board = parse_board(source_code)
    board.substitute("A", a)
    board.substitute("B", b)
    history = [board]
    min_x = board.min_x
    max_x = board.max_x
    min_y = board.min_y
    max_y = board.max_y
    max_time = 1

    for tick in range(1_000_000):
        min_x = min(min_x, board.min_x)
        max_x = max(max_x, board.max_x)
        min_y = min(min_y, board.min_y)
        max_y = max(max_y, board.max_y)
        time = len(history)
        max_time = max(max_time, time)
        if verbose:
            print(f"[time={time}, tick={tick}, x={board.min_x}, y={board.min_y}]")
            print(board)

        erasures: List[Coordinate] = []
        reductions: Dict[Coordinate, List[Element]] = defaultdict(list)
        rollbacks: Dict[Tuple[int, Coordinate], List[Element]] = defaultdict(list)
        for (x, y), element in board.operators.items():
            if isinstance(element, int):
                continue
            elif element in "SAB":
                continue
            elif element in "<>v^":
                destination = {
                    "<": (x, y-1),
                    ">": (x, y+1),
                    "^": (x-1, y),
                    "v": (x+1, y),
                }[element]
                source = {
                    "<": (x, y+1),
                    ">": (x, y-1),
                    "^": (x+1, y),
                    "v": (x-1, y),
                }[element]
                if board[source] == ".":
                    continue
                erasures.append(source)
                reductions[destination].append(board[source])
            elif element in "+-*/%":
                left_source = x, y-1
                right_source = x-1, y
                destinations = [(x+1, y), (x, y+1)]
                if not isinstance(board[left_source], int) or not isinstance(board[right_source], int):
                    continue
                left, right = board[left_source], board[right_source]
                if element in "+-*":
                    result = eval(f"{left} {element} {right}")
                elif element == "/":
                    if right < 0:
                        left, right = -left, -right
                    result = left // right
                elif element == "%":
                    result = abs(left) % abs(right)
                    if right < 0:
                        result *= -1
                else:
                    raise ValueError(f"unreachable: unknown arithmetic operand {element}")
                erasures += [left_source, right_source]
                for destination in destinations:
                    reductions[destination].append(result)
            elif element in "=#":
                left_source = x-1, y
                right_source = x, y-1
                left_destination = x, y+1
                right_destination = x+1, y
                left, right = board[left_source], board[right_source]
                if left == "." or right == ".":
                    continue
                if element == "=" and left != right:
                    continue
                if element == "#" and left == right:
                    continue
                erasures += [left_source, right_source]
                reductions[left_destination].append(left)
                reductions[right_destination].append(right)
            elif element == "@":
                dx = board[x, y-1]
                value = board[x-1, y]
                dy = board[x, y+1]
                dt = board[x+1, y]
                if not isinstance(dx, int):
                    continue
                if not isinstance(dy, int):
                    continue
                if not isinstance(dt, int):
                    continue
                if value == ".":
                    continue
                if dt <= 0:
                    raise ValueError(f"time warp to future is not allowed. dt={dt}")
                destination = x - dy, y - dx  # x, y is confused here
                rollback_time = time - dt
                rollbacks[rollback_time, destination].append(value)

        for coordinate, writes in reductions.items():
            if len(writes) > 1:
                raise ValueError(f"conflict reduction at {coordinate}")
        
        submissions = set()
        for coordinate, writes in reductions.items():
            if coordinate not in board.submission_places:
                continue
            submissions.add(writes[0])
        if len(submissions) > 1:
            raise ValueError(f"multiple submissions detected: {submissions}")
        if len(submissions) == 1:
            answer = next(iter(submissions))
            complexity = (max_x + 1 - min_x) * (max_y + 1 - min_y) * max_time
            return answer, complexity
        
        rollback_times = set(rollback_time for rollback_time, coordinate in rollbacks.keys())
        if len(rollback_times) > 1:
            raise ValueError(f"attempted to travel to different times: {rollback_times}")
        if len(rollback_times) == 1:
            rollback_time = next(iter(rollback_times))

            destination_board = history[rollback_time - 1]
            history = history[:rollback_time - 1]
            next_operators = destination_board.operators.copy()

            time_travel_submissions: Dict[Coordinate, List[Element]] = defaultdict(list)
            for (_rollback_time, coordinate), writes in rollbacks.items():
                if len(set(writes)) > 1:
                    raise ValueError(f"attempted to write different values to {coordinate} during time travel")
                next_operators[coordinate] = writes[0]
                if coordinate in destination_board.submission_places:
                    time_travel_submissions[coordinate].append(writes[0])
            if len(time_travel_submissions) > 1:
                raise ValueError(f"attempted to submit from multiple places during time travel")
            if len(time_travel_submissions) == 1:
                answer = next(iter(time_travel_submissions))[0]
                complexity = (max_x + 1 - min_x) * (max_y + 1 - min_y) * max_time
                return answer, complexity
            board = Board(next_operators)
            history.append(board)
            continue

        if len(erasures) + len(reductions) + len(rollbacks) == 0:
            raise ValueError("no reduce occured.")

        next_operators = board.operators.copy()
        for erasure in set(erasures):
            del next_operators[erasure]
        for coordinate, writes in reductions.items():
            next_operators[coordinate] = writes[0]
        board = Board(next_operators)
        history.append(board)

    raise TimeoutError("tick limit exceeded.")


def main():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="writes all steps")
    parser.add_argument("source_file", help="source code file")
    parser.add_argument("a_value", type=int, help="input A")
    parser.add_argument("b_value", type=int, help="input B")

    args = parser.parse_args()
    with open(args.source_file) as f:
        source_code = f.read()
        answer, complexity = run(source_code, args.a_value, args.b_value, args.verbose)
        print(f"submission: {answer}")
        print(f"complexity: {complexity}")
        

if __name__ == "__main__":
    main()
