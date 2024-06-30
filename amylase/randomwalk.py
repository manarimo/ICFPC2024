# this output solves lambdaman5 (roll cake)

import random
import io


class RNG:
    def __init__(self, initial_state: int) -> None:
        self.state = initial_state
    
    def get_integer(self) -> int:
        self.state = 48271 * self.state % ((2 ** 31) - 1)
        return self.state


def main():
    rng = random.Random()
    rng = RNG(11111)
    buf = io.StringIO()
    for _ in range(1000000):
        d = "UDRL"[rng.get_integer() % 4]
        buf.write(d)
    print(buf.getvalue())


if __name__ == "__main__":
    main()
