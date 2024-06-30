import { useState } from 'react'
import './App.css'
import LambdamanSimulator from './LambdamanSimulator'

function App() {
  const [problem, setProblem] = useState("###.#...\n...L..##\n.#######")

  const [patterns, setPatterns] = useState(["LLLDURRRUDRRURR"])
  const [moves, setMoves] = useState("0")

  const solution = moves.split('').map((move) => patterns[parseInt(move)]).join('')  
  const width = 80
  return (
    <>
      <div>
        <textarea value={problem} cols={width} rows={10} onChange={(e) => setProblem(e.target.value)}/>
      </div>

      <div>
        <input type='text' value={solution} size={width} readOnly />
      </div>

      <div>
        <div>
          {patterns.map((pattern, i) => {
            return (
              <div key={`pattern-${i}`}>
                <span>Pattern {i}: </span>
                <input type='text' value={pattern} onChange={(e) => { 
                  const newPatterns = patterns.concat()
                  newPatterns[i] = e.target.value
                  setPatterns(newPatterns) 
                }}/>
                <button type='button' onClick={() => setPatterns(patterns.slice(0, i).concat(...patterns.slice(i + 1))) }>del</button>
              </div>
            )
          })}
        </div>
        <div>
          <button type='button' onClick={() => setPatterns(patterns.concat("")) }>add</button>
        </div>
      </div>

      <div>
      <span>Moves: </span>
      <input type='text' value={moves} onChange={(e) => setMoves(e.target.value)} />
      </div>

      <div>
        <LambdamanSimulator problem={problem} solution={solution}/>
      </div>
    </>
  )
}

export default App
