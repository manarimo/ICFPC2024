import { useState } from "react";
import { Board } from "../runner";

type Snapshots = {
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
  maxTime: number;
  snapshots: {
    time: number;
    board: Board;
  }[];
};

export const useSnapshots = () => {
  const [snapshots, setSnapshots] = useState<Snapshots | null>(null);
  return {
    snapshots,
    setSnapshots,
  };
};
