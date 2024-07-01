type Coordinate = `${number},${number}`;
type Element = Operator | bigint | ".";
const coord = (c: Coordinate) => {
  const [i, j] = c.split(",");
  return { i: Number(i), j: Number(j) };
};

export type Board = {
  operators: Map<Coordinate, Element>;
};

const OPERATORS = [
  "<",
  ">",
  "^",
  "v",
  "+",
  "-",
  "*",
  "/",
  "%",
  "@",
  "=",
  "#",
  "S",
  "A",
  "B",
] as const;
type Operator = (typeof OPERATORS)[number];

const run = (
  sourceCode: string,
  a: bigint,
  b: bigint,
  timeLimit: number = 1_000_000,
  debug: boolean = false
) => {
  let board = parseBoard(sourceCode);
  board = substitute(board, "A", a);
  board = substitute(board, "B", b);

  const history = [board];
  const stats = statistics(board);
  let minX = stats.minX;
  let maxX = stats.maxX;
  let minY = stats.minY;
  let maxY = stats.maxY;
  let maxTime = 1;

  const snapshots = [];
  for (let tick = 0; tick < timeLimit; tick++) {
    const currentStats = statistics(board);
    const submissionPlaces = currentStats.submissionPlaces;

    minX = Math.min(minX, currentStats.minX);
    maxX = Math.max(maxX, currentStats.maxX);
    minY = Math.min(minY, currentStats.minY);
    maxY = Math.max(maxY, currentStats.maxY);
    const time = history.length;
    maxTime = Math.max(maxTime, time);
    if (debug) {
      console.log(
        `tick=${tick}, time=${time}, minX=${minX}, maxX=${maxX}, minY=${minY}, maxY=${maxY}`
      );

      const h = maxX - minX + 1;
      const w = maxY - minY + 1;
      const matrix = Array.from({ length: h }, () =>
        Array.from({ length: w }, () => ".")
      );
      board.operators.forEach((element, key) => {
        const { i, j } = coord(key);
        matrix[i - minX][j - minY] = element === "." ? "." : `${element}`;
      });

      console.log(matrix.map((row) => row.join(" ")).join("\n"));
    }

    console.log(`tick=${tick} time=${time}`);
    snapshots.push({ time, board });

    const erasures: Coordinate[] = [];
    const reductions = new Map<Coordinate, Element[]>();
    const rollbacks = new Map<`${number},${number},${number}`, Element[]>();

    for (const [key, element] of board.operators) {
      const { i, j } = coord(key);
      if (typeof element === "bigint") {
        continue;
      }
      if (["S", "A", "B"].includes(element)) {
        continue;
      }

      const op = (["<", "v", ">", "^"] as const).find((op) => op === element);
      if (op) {
        const destination = (
          {
            "<": `${i},${j - 1}`,
            ">": `${i},${j + 1}`,
            "^": `${i - 1},${j}`,
            v: `${i + 1},${j}`,
          } as const
        )[op];
        const source = (
          {
            "<": `${i},${j + 1}`,
            ">": `${i},${j - 1}`,
            "^": `${i + 1},${j}`,
            v: `${i - 1},${j}`,
          } as const
        )[op];

        const value = board.operators.get(source);
        if (value === "." || value === undefined) {
          continue;
        }

        erasures.push(source);
        const reduction = reductions.get(destination) ?? [];
        reduction.push(value);
        reductions.set(destination, reduction);
        continue;
      }

      const binop = (["+", "-", "*", "/", "%"] as const).find(
        (op) => op === element
      );
      if (binop) {
        const leftSouce: `${number},${number}` = `${i},${j - 1}`;
        const rightSource: `${number},${number}` = `${i - 1},${j}`;
        const destinations: `${number},${number}`[] = [
          `${i + 1},${j}`,
          `${i},${j + 1}`,
        ];

        const left = board.operators.get(leftSouce);
        const right = board.operators.get(rightSource);
        if (typeof left !== "bigint" || typeof right !== "bigint") {
          continue;
        }

        let result = 0n;
        if (binop === "+") {
          result = left + right;
        } else if (binop === "-") {
          result = left - right;
        } else if (binop === "*") {
          result = left * right;
        } else if (binop === "/") {
          if (right === 0n) {
            continue;
          }
          result = abs(left) / abs(right);
          if (left * right < 0n) {
            result = -result;
          }
        } else if (binop === "%") {
          if (right === 0n) {
            continue;
          }
          result = abs(left) % abs(right);
          if (left < 0n) {
            result *= -1n;
          }
        } else {
          const nv: never = binop;
          console.error(nv);
        }

        erasures.push(leftSouce);
        erasures.push(rightSource);
        destinations.forEach((destination) => {
          const reduction = reductions.get(destination) ?? [];
          reduction.push(result);
          reductions.set(destination, reduction);
        });

        continue;
      }

      const logicop = (["=", "#"] as const).find((op) => op === element);
      if (logicop) {
        const uSource: `${number},${number}` = `${i - 1},${j}`;
        const lSource: `${number},${number}` = `${i},${j - 1}`;
        const uDestination: `${number},${number}` = `${i},${j + 1}`;
        const lDestination: `${number},${number}` = `${i + 1},${j}`;

        const u = board.operators.get(uSource) ?? ".";
        const l = board.operators.get(lSource) ?? ".";
        if (u === "." || l === ".") {
          continue;
        }
        if (logicop === "=" && u !== l) {
          continue;
        }
        if (logicop === "#" && u === l) {
          continue;
        }

        erasures.push(uSource);
        erasures.push(lSource);
        const uReduction = reductions.get(uDestination) ?? [];
        uReduction.push(u);
        reductions.set(uDestination, uReduction);

        const lReduction = reductions.get(lDestination) ?? [];
        lReduction.push(l);
        reductions.set(lDestination, lReduction);

        continue;
      }

      if (element === "@") {
        const dx = board.operators.get(`${i},${j - 1}`);
        const value = board.operators.get(`${i - 1},${j}`) ?? ".";
        const dy = board.operators.get(`${i},${j + 1}`);
        const dt = board.operators.get(`${i + 1},${j}`);
        if (
          typeof dx !== "bigint" ||
          typeof dy !== "bigint" ||
          typeof dt !== "bigint"
        ) {
          continue;
        }
        if (value === ".") {
          continue;
        }
        if (dt <= 0n) {
          return {
            type: "error" as const,
            message: `time warp to future is not allowed. dt={dt}`,
            minX,
            maxX,
            minY,
            maxY,
            maxTime,
            snapshots,
          };
        }

        const rollbackTime = time - Number(dt);
        const rollback =
          rollbacks.get(
            `${i - Number(dy)},${j - Number(dx)},${rollbackTime}`
          ) ?? [];
        rollback.push(value);
        rollbacks.set(
          `${i - Number(dy)},${j - Number(dx)},${rollbackTime}`,
          rollback
        );
      }
    }

    for (const [coordinate, writes] of reductions) {
      if (writes.length > 1) {
        return {
          type: "error" as const,
          message: `conflict reduction at ${coordinate}`,
          minX,
          maxX,
          minY,
          maxY,
          maxTime,
          snapshots,
        };
      }
    }

    const submissions = new Set<Element>();
    reductions.forEach((writes, coordinate) => {
      if (submissionPlaces.includes(coordinate)) {
        submissions.add(writes[0]);
      }
    });

    if (submissions.size > 1) {
      return {
        type: "error" as const,
        message: `conflict submission at ${submissions}`,
        minX,
        maxX,
        minY,
        maxY,
        maxTime,
        snapshots,
      };
    }

    if (submissions.size === 1) {
      const answer = Array.from(submissions)[0];
      const complexity = (maxX + 1 - minX) * (maxY + 1 - minY) * maxTime;
      return {
        type: "success" as const,
        answer,
        complexity,
        minX,
        maxX,
        minY,
        maxY,
        maxTime,
        snapshots,
      };
    }

    const rollbackTimes = new Set(
      Array.from(rollbacks.keys()).map((key) => key.split(",")[2])
    );
    if (rollbackTimes.size > 1) {
      return {
        type: "error" as const,
        message: `conflict rollback at ${rollbackTimes}`,
        minX,
        maxX,
        minY,
        maxY,
        maxTime,
        snapshots,
      };
    }

    if (rollbackTimes.size === 1) {
      const rollbackTime = Number(Array.from(rollbackTimes)[0]);
      if (rollbackTime < 1) {
        return {
          type: "error" as const,
          message: `rollback to past is not allowed. rollbackTime=${rollbackTime}`,
          minX,
          maxX,
          minY,
          maxY,
          maxTime,
          snapshots,
        };
      }
      const destinationBoard = history[rollbackTime - 1];
      const destinationStats = statistics(destinationBoard);
      while (history.length > rollbackTime - 1) {
        history.pop();
      }
      const nextOperators = new Map(destinationBoard.operators);

      const timeTravelSubmissions = new Map<Coordinate, Element[]>();
      rollbacks.forEach((writes, key) => {
        const [i, j] = key.split(",").map(Number);
        nextOperators.set(`${i},${j}`, writes[0]);
        const submissionPlaces = destinationStats.submissionPlaces;
        if (submissionPlaces.includes(`${i},${j}`)) {
          const submissions = timeTravelSubmissions.get(`${i},${j}`) ?? [];
          submissions.push(writes[0]);
          timeTravelSubmissions.set(`${i},${j}`, submissions);
        }
      });
      if (timeTravelSubmissions.size > 1) {
        return {
          type: "error" as const,
          message: `conflict submission at ${timeTravelSubmissions}`,
          minX,
          maxX,
          minY,
          maxY,
          maxTime,
          snapshots,
        };
      }
      if (timeTravelSubmissions.size === 1) {
        const answer = Array.from(timeTravelSubmissions.values())[0][0];
        const complexity = (maxX + 1 - minX) * (maxY + 1 - minY) * maxTime;
        return {
          type: "success" as const,
          answer,
          complexity,
          minX,
          maxX,
          minY,
          maxY,
          maxTime,
          snapshots,
        };
      }

      board = { operators: nextOperators };
      history.push(board);
      continue;
    }

    if (erasures.length + reductions.size + rollbacks.size === 0) {
      return {
        type: "error" as const,
        message: `no reductions`,
        minX,
        maxX,
        minY,
        maxY,
        maxTime,
        snapshots,
      };
    }

    const nextOperators = new Map(board.operators);
    erasures.forEach((key) => {
      nextOperators.delete(key);
    });
    reductions.forEach((writes, key) => {
      nextOperators.set(key, writes[0]);
    });
    board = { operators: nextOperators };
    history.push(board);
  }

  return {
    type: "error" as const,
    message: `time limit exceeded. timeLimit=${timeLimit}`,
    minX,
    maxX,
    minY,
    maxY,
    maxTime,
    snapshots,
  };
};

const parseBoard = (sourceCode: string) => {
  const operators = new Map<`${number},${number}`, Element>();
  const lines = sourceCode.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line === "") continue;
    const tokens = line.split(/[\s\t]+/);
    for (let j = 0; j < tokens.length; j++) {
      const token = tokens[j];
      if (token === ".") {
        continue;
      }

      const op = OPERATORS.find((op) => op === token);
      if (op) {
        operators.set(`${i},${j}`, op);
      } else {
        const value = Number(token);
        if (Number.isInteger(value) && -99 <= value && value <= 99) {
          operators.set(`${i},${j}`, BigInt(value));
        } else {
          throw new Error(`invalid token: ${token}`);
        }
      }
    }
  }
  return { operators };
};

const substitute = (board: Board, operator: Operator, n: bigint) => {
  const newBoard = new Map<Coordinate, Element>();
  board.operators.forEach((value, key) => {
    if (value === operator) {
      newBoard.set(key, n);
    } else {
      newBoard.set(key, value);
    }
  });
  return { operators: newBoard };
};

const statistics = (board: Board) => {
  const submissionPlaces = [] as Coordinate[];
  let minX = Infinity;
  let maxX = -Infinity;
  let minY = Infinity;
  let maxY = -Infinity;
  board.operators.forEach((element, key) => {
    const { i, j } = coord(key);
    minX = Math.min(minX, i);
    maxX = Math.max(maxX, i);
    minY = Math.min(minY, j);
    maxY = Math.max(maxY, j);
    if (element === "S") {
      submissionPlaces.push(key);
    }
  });

  return { minX, maxX, minY, maxY, submissionPlaces };
};

const abs = (b: bigint) => (b < 0n ? -b : b);

export default run;
