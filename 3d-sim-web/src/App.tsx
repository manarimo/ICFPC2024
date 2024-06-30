import useEditor from "./hooks/useEditor";
import { useLoadInput } from "./hooks/useLoadInput";

function App() {
  const { text, setText, a, setA, b, setB, timeLimitText, setTimeLimitText } =
    useEditor();
  const { loadInput } = useLoadInput();
  return (
    <div>
      <div>a</div>
      <button
        onClick={() => {
          const result = loadInput({ sourceCode: text, a, b, timeLimitText });
          if (result.type === "error") {
            alert(result.message);
            return;
          }
        }}
      >
        Load
      </button>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          gap: 20,
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
          }}
        >
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={30}
            cols={40}
          />
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
          }}
        >
          <div style={{ display: "flex", flexDirection: "row" }}>
            <p>A:</p>
            <input
              type="number"
              value={a}
              onChange={(e) => setA(e.target.value)}
            />
          </div>
          <div style={{ display: "flex", flexDirection: "row" }}>
            <p>B:</p>
            <input
              type="number"
              value={b}
              onChange={(e) => setB(e.target.value)}
            />
          </div>
          <div style={{ display: "flex", flexDirection: "row" }}>
            <p>Timelimit:</p>
            <input
              type="number"
              value={timeLimitText}
              onChange={(e) => setTimeLimitText(e.target.value)}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
