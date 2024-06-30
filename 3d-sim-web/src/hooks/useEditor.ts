import { useState } from "react";

const useEditor = () => {
  const [text, setText] = useState("");
  const [a, setA] = useState("0");
  const [b, setB] = useState("0");

  const [timeLimitText, setTimeLimitText] = useState("100");

  return {
    text,
    setText,
    a,
    b,
    setA,
    setB,
    timeLimitText,
    setTimeLimitText,
  };
};

export default useEditor;
