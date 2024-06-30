import { useCallback } from "react";
import run from "../runner";

export const useLoadInput = () => {
  const loadInput = useCallback(
    ({
      sourceCode,
      a,
      b,
      timeLimitText,
    }: {
      sourceCode: string;
      a: string;
      b: string;
      timeLimitText: string;
    }) => {
      const aValue = Number(a);
      if (!Number.isInteger(aValue)) {
        return {
          type: "error" as const,
          message: "A must be an integer",
        };
      }
      const bValue = Number(b);
      if (!Number.isInteger(bValue)) {
        return {
          type: "error" as const,
          message: "B must be an integer",
        };
      }
      const timeLimit = Number(timeLimitText);
      if (!Number.isInteger(timeLimit)) {
        return {
          type: "error" as const,
          message: "Timelimit must be an integer",
        };
      }

      try {
        const result = run(sourceCode, BigInt(aValue), BigInt(bValue));
        if (result.type === "error") {
          return {
            ...result,
            type: "executionError" as const,
          };
        } else if (result.type === "success") {
          return result;
        } else {
          const nv: never = result;
          return nv;
        }
      } catch (error) {
        return {
          type: "error" as const,
          message: `${error}`,
        };
      }
    },
    []
  );

  return {
    loadInput,
  };
};
