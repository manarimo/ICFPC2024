import { useState } from "react";

const useEditor = () => {
  const [text, setText] = useState("");
  const [a, setA] = useState("");
  const [b, setB] = useState("");

  const [timeLimitText, setTimeLimitText] = useState("1000");

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
