# Lambdaman

After writing a DFS, I was stuck and didn't know what to do next. I thought about doing TSP if I were to be serious about it, but I didn't want to write it. So, I considered if I could solve just the maze part with a simple algorithm and thought about right-hand rule-like methods. However, without feedback from the walls, it seemed impossible.

I thought small patterns might be manageable through repetition. I examined all patterns up to a length of 12 but eventually gave up as it wasn't feasible.

After giving up on Lambdaman, I manually solved Lambdaman and worked on improving small cases for 3D problems.

# 3D1
This involved calculating factorials. The approach was to transform A∗(A−1)+... into 1∗2∗... with hardcoding the checks for A=1 and A=2.

# 3D3
The goal was to determine the sign. There were two approaches: 
- To keep dividing by 2 until it became 1 or -1,
- To compute (A+1)%2 + A%2.

I focused on the former, but the latter turned out to be the correct approach.

For the sake of short coding, I used a trick to overwrite the condition check for A=0 by A=−1 check.

# 3D4
This was about determining the maximum value between A and B. Initially, I incremented A+1 and B+1 separately. By incrementing one by one while swapping A and B, it became more compact.

# 3D5
For calculating the LCM of A and B, I looked at other people's solutions and removed unnecessary TimeWarp operations. By tweaking it, I managed to make it slightly smaller. Key trick was changing the terminal condition of the Euclidean algorithm; originally it was adding 0 to terminate the loop, and I modified it to overwrite an operator that was placed to move away S operator.
