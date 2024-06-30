import { Board } from ".";

export const boardToMatrix = ({
  board,
  minX,
  maxX,
  minY,
  maxY,
}: {
  board: Board;
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
}) => {
  const h = maxX - minX + 1;
  const w = maxY - minY + 1;
  const matrix = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => ".")
  );
  board.operators.forEach((element, key) => {
    const [i, j] = key.split(",").map(Number);
    matrix[i - minX][j - minY] = element === "." ? "." : `${element}`;
  });
  return matrix;
};
