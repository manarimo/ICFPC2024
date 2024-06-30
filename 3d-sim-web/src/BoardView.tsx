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
    const viewBox = `0 0 ${width} ${height}`;

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
            <text key={`${i}-${j}`} y={i * W} x={j * W} width={W} height={W}>
              {cell}
            </text>
          ))}
      </svg>
      <p>time = {board.time}</p>
    </div>
  );
};

export default BoardView;
