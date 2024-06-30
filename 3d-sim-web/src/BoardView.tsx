import { FC, useMemo } from "react";
import { useSnapshots } from "./hooks/useSnapshots";
import { boardToMatrix } from "./runner/board";

const W = 30;

type Snapshots = ReturnType<typeof useSnapshots>["snapshots"];

type Props = {
  snapshots: Snapshots;
  pos: number;
};

const BoardView: FC<Props> = ({ snapshots, pos }) => {
  const board = useMemo(() => {
    if (!snapshots) return null;
    const matrix = boardToMatrix({
      board: snapshots.snapshots[pos].board,

      maxX: snapshots.maxX,
      maxY: snapshots.maxY,
      minX: snapshots.minX,
      minY: snapshots.minY,
    });
    return { matrix, time: snapshots.snapshots[pos].time };
  }, [pos, snapshots]);
  const params = useMemo(() => {
    if (!snapshots) return null;
    const height = (snapshots.maxX - snapshots.minX + 1) * W;
    const width = (snapshots.maxY - snapshots.minY + 1) * W;
    const viewBox = `0 0 ${width + 2 * W} ${height + 2 * W}`;

    return {
      height,
      width,
      viewBox,
    };
  }, [snapshots]);

  if (!board || !params) {
    return null;
  }

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <svg {...params}>
        {board.matrix
          .flatMap((row, i) => row.map((cell, j) => ({ cell, i, j })))
          .map(({ cell, i, j }) => (
            <g>
              <title>{cell}</title>
              <text
                key={`${i}-${j}`}
                y={i * W + W}
                x={j * W + W}
                fontSize={calcFontSize(cell)}
                textAnchor="middle"
                dominantBaseline="middle"
              >
                {cell}
              </text>
            </g>
          ))}
      </svg>
      <p>time = {board.time}</p>
    </div>
  );
};

export default BoardView;

const calcFontSize = (cell: string) => {
  const size = (W / Math.max(cell.length, 1)) * 0.9;
  return `${size}px`;
};
