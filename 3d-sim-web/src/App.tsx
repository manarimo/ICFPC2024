import BoardView from "./BoardView";
import useEditor from "./hooks/useEditor";
import { useLoadInput } from "./hooks/useLoadInput";
import { useSnapshots } from "./hooks/useSnapshots";
import { useSlider } from "./hooks/useSlider";

function App() {
  const { text, setText, a, setA, b, setB, timeLimitText, setTimeLimitText } =
    useEditor();
  const { loadInput } = useLoadInput();
  const { snapshots, setSnapshots } = useSnapshots();
  const slider = useSlider(snapshots?.snapshots.length);

  return (
    <div>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <BoardView snapshots={snapshots} pos={slider.pos} />
        <input
          type="range"
          min="0"
          max={(snapshots?.snapshots.length ?? 1) - 1}
          value={slider.pos}
          onChange={(e) => slider.setPos(Number(e.target.value))}
        />
      </div>
      <button
        onClick={() => {
          const result = loadInput({ sourceCode: text, a, b, timeLimitText });
          if (result.type === "error") {
            alert(result.message);
            return;
          }

          const { maxX, minX, maxY, minY, maxTime, snapshots } = result.result;
          setSnapshots({
            maxX,
            minX,
            maxY,
            minY,
            maxTime,
            snapshots,
          });
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
