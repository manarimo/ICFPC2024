import { useState } from 'react'
import './App.css'
import LambdamanSimulator from './LambdamanSimulator'

function App() {
  const [problem, setProblem] = useState("###.#...\n...L..##\n.#######")
  const [solution, setSolution] = useState("LLLDURRRUDRRURR")

  const [patterns, setPatterns] = useState([])
  const [moves, setMoves] = useState("")

  const width = 80
  return (
    <>
      <div>
        <textarea value={problem} cols={width} rows={10} onChange={(e) => setProblem(e.target.value)}/>
      </div>

      <div>
        <input type='text' value={solution} size={width} onChange={(e) => setSolution(e.target.value)}/>
      </div>

      <div>
        <LambdamanSimulator problem={problem} solution={solution}/>
      </div>
    </>
  )
}

export default App