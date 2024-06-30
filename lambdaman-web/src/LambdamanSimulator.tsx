import { useState } from 'react'

type Props = {
    problem: string
    solution: string
}

enum Cell {
    EMPTY,
    WALL,
    PILL,
}

function cellChar(cell: Cell) {
    switch (cell) {
        case Cell.EMPTY:
            return ' '
        case Cell.WALL:
            return '#'
        case Cell.PILL:
            return '.'
    }
}

function getVector(move: string): [number, number] {
    if (move === "L") {
        return [0, -1]
    } else if (move === "R") {
        return [0, 1]
    } else if (move === "D") {
        return [1, 0]
    } else if (move === "U") {
        return [-1, 0]
    } else {
        throw `invalid move: ${move}`
    }
}

class State {
    board: Cell[][]
    lambdamanRow: number
    lambdamanCol: number

    constructor(board: Cell[][], lambdamanRow: number, lambdamanCol: number) {
        this.board = board
        this.lambdamanRow = lambdamanRow
        this.lambdamanCol = lambdamanCol
    }
    
    static fromProblem(problem: string): State {
        let lambdamanRow = -1, lambdamanCol = -1
        const board = problem.trim().split("\n")
            .map((row, ri) => 
                row.split('').map((c, ci) => {
                    if (c === '#') {
                        return Cell.WALL
                    } else if (c === '.') {
                        return Cell.PILL
                    } else if (c === 'L') {
                        lambdamanRow = ri
                        lambdamanCol = ci
                        return Cell.EMPTY
                    } else {
                        return Cell.EMPTY
                    }
                })
            )
        if (lambdamanCol < 0) {
            throw "lambdaman not found"
        }
        return new State(board, lambdamanRow, lambdamanCol)
    }

    rows(): number {
        return this.board.length
    }

    cols(): number {
        return this.board[0].length
    }

    move(directions: string) {
        for (let i = 0; i < directions.length; i++) {
            const direction = directions[i]
            const [dr, dc] = getVector(direction)
            const nr = this.lambdamanRow + dr
            const nc = this.lambdamanCol + dc
            if (nr < 0 || nr >= this.rows() || nc < 0 || nc >= this.cols()) {
                return
            }
            if (this.board[nr][nc] === Cell.WALL) {
                return
            }
            this.board[nr][nc] = Cell.EMPTY
            this.lambdamanRow = nr
            this.lambdamanCol = nc
        } 
    }

    pills(): number {
        let count = 0;
        for (let r = 0; r < this.rows(); r++) {
            for (let c = 0; c < this.cols(); c++) {
                if (this.board[r][c] === Cell.PILL) {
                    count += 1
                }
            }
        }
        return count
    }

    toString(): string {
        return this.board.map((row, ri) => {
            return row.map((cell, ci) => {
                if (ri === this.lambdamanRow && ci === this.lambdamanCol) {
                    return 'L'
                } else {
                    return cellChar(cell)
                }
            }).join('')
        }).join('\n')
    }
}


function simulate(problem: string, steps: string): State {
    const state = State.fromProblem(problem)
    state.move(steps)
    return state
}

function StateView(props: { state: State }) {
    const { state } = props
    return (
        <div>
            <textarea style={ {fontFamily: "monospace"} } value={state.toString()} cols={state.cols()} rows={state.rows()} readOnly/>
        </div>
    )
}

function LambdamanSimulator(props: Props) {
    const [step, setStep] = useState(0)
    const currentState = simulate(props.problem, props.solution.substring(0, step))
    const finalState = simulate(props.problem, props.solution)
    const isSuccess = finalState.pills() === 0

    return (
        <div>
            <div>
                <span>Solution: </span>
                <div>
                    {props.solution}
                </div>
            </div>

            <div>
                <span>isSuccess: {isSuccess ? "Success" : "Failure"}</span>
            </div>

            <div>
                <span>State: </span>
                <StateView state={currentState} />
            </div>

            <div>
                <span>Step: </span>
                <div>
                    {`${step} / ${props.solution.length}`}
                </div>
                <input type='range' 
                    min={0} max={props.solution.length} step={1} value={step}
                    onChange={e => setStep(parseInt(e.target.value))} 
                />
            </div>
        </div>
    )
}

export default LambdamanSimulator
