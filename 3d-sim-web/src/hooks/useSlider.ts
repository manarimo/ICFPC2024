import { useEffect, useState } from "react";

export const useSlider = (length: number | undefined) => {
  const [pos, setPos] = useState(0);
  useEffect(() => {
    if (length && length <= pos) {
      setPos(length - 1);
    }
  }, [length, pos]);

  return {
    pos,
    setPos,
  };
};
