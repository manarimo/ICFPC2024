Japanese: [all.md](./all.md)

Translations powered by ChatGPT + manual touch-up.

# amylase
## Lambdaman

Using one character for each of LRDU is clearly inefficient, so I considered encoding. On the first day, I managed to come up with a fairly effective encoding that was reasonably short.

After that, I had no new ideas and stalled for over a day. As answers exceeding the theoretical limits of information theory appeared in the rankings, I realized that the compression approach would never win, so I started over. On Sunday night, I finally came up with the idea of a random walk. Although my team members were quite skeptical, trying it out was quick, and when I managed to solve lambdaman4, I was convinced this was the solution.

For the random number generation used in the random walk, I chose the linear congruential method because it’s simple to implement. When looking up coefficients on Wikipedia, I found a setting without a constant term: next = (48271 * x) % (2 << 31 - 1), which was advantageous for code golfing, so I adopted it.

Upon reflection, I realized this worked because the modulus is a (Mersenne) prime and 48271 is likely a primitive root, thus maximizing the period. I discovered that if the parameters meet the same conditions, smaller ones would result in shorter code. Then, I just wrote the program and ran it. Specific generator code was shrunk significantly by osak’s exceptional code golfing, so I’m not entirely sure about the details.


## Efficiency
- 1: When the source code is executed, it obviously doesn’t stop, but reading the code shows it’s applying a quadrupling operation 22 times.
- 2: I found that a large loop was running but multiplying the result by 0. At this point, I realized it was a game of code reading.

I read through several more, but didn’t solve some myself, such as problems 7-11 which used a SAT solver.

# kawatea
## Spaceship

Since there were no walls or winds like in the AtCoder Masters Final (https://atcoder.jp/contests/masters2024-final), I wrote a greedy algorithm to move precisely to the next vertex.

Upon re-reading the problem statement, I realized the order was not fixed, so I sorted the input by coordinates.

To further improve the order, I solved the TSP using the distance from the greedy method as the cost.

By playing around with small problems by hand to gain better insights, I noticed that many problems could be solved by filling in gaps in the order, if the order was set well.

For the TSP order, I wrote a beam search that considered the state as the vertices visited and the current speed, with transitions to the next vertex. The movement commands were exhaustively searched up to about five moves.

I also tried a version that didn’t fix the visiting order and flagged the visited vertices, but it didn’t make much difference.

For larger problems with greater distances between vertices that couldn't be solved this way, I wrote another beam search treating each transition as a single command.

For some problems where the best solution wasn’t quite reached, the TSP order didn’t seem optimal, so I wrote simulated annealing to slightly change the order. The transitions for the annealing included moving one vertex to another place, moving a continuous section of vertices to another place, and reversing a continuous section of vertices.

I kept tweaking the parameters of the beam search and simulated annealing, running them repeatedly.

# kenkoooo
## Efficiency

- When I looked at the code, it was creating recursive functions using a fixed-point combinator.
- Problems 7 and 8 boil down to something like "find the smallest x that satisfies the logical expressions between each bit (many of them)," so they can be solved using a SAT solver.
- While the above was dealing with the relationships of each digit in binary, problems 9 to 11 solve logical expressions for each digit in base-9. This becomes a 9-coloring problem (I later heard it was like Sudoku), so I used an LP solver.

# mkut
## 3D1
A loop is necessary, but kindly, the example explains how to create and exit a loop using Time Warp, so I just did the same.

## 3D2
At first, I thought it was impossible without comparisons, but since the input range is small, I tried values from 0 sequentially until it became A or -A. Although a method using A\*sign(A) also emerged, I eventually returned to this solution.

## 3D3
Change 3D2 so that, if the result is root of -A, then \*0-1, or is A, then \*0+1, and if it's 0, then just output 0. On the second day, I woke up and someone had left a brilliant idea that if it’s odd then A%2 is the answer, so I refined that. I didn't realize until the end that it wouldn't die from zero division.

## 3D4
Increment A and B continuously, and when one becomes the other, that's the answer. It was apparently the best solution when arranged neatly.

## 3D5
Just do A\*B/GCD(A, B). It was difficult to avoid division by zero, but it turned out to be unnecessary.

## 3D6
Just try dividing sequentially from 2. The initial code I wrote had a good ranking, so I left it for a long time. However, since the other problems were too difficult, I tweaked it a bit in a few minutes, and it became the best solution.

## 3D7
Consider the n-ary number as a stack, and if it doesn’t change when rearranged, it's a palindrome.

## 3D8
Just loop 3D7, but you need to update the constant 10 you wrote. I devised a subroutine notation (\*\*) to use for updating the values.

(\*\*) Set the period shorter than others, compare input with #, and restore the input to its original value during execution to run once without affecting other programs.

## 3D9
Looking from the end, if ')' comes, add 1, and if '(' comes, subtract 1. If it becomes -1 midway, it's NG. If it ends at 0, it's OK.

## 3D10
Using a stack would have solved it, but initially, I was struggling to update (the stack of consecutive same parentheses, the leading character of the stack), which was a nightmare.

## 3D11
I considered treating the board as memory, but gave up since reading was tough (someone told me it would get TLE anyway because the program was too large). I tried encoding the number of times coordinates were visited from 200\*200 into an integer up to 100^(200\*200), but it TLE'd at the maximum case of 20k steps (limit is 1M steps). When I had the stack of visited coordinates and spent O(N) to avoid duplicate insertion, the integer became up to (200\*200)^100 and it became faster? and it passed. Since the goal was just to pass, I didn't optimize the layout for this one.

## 3D12
At first glance, it looks bad, but just do a Taylor expansion. Initially, I thought no error was allowed and tried various things, but then I realized an error of 1 was acceptable, so I just multiplied by 99 and divided by 99 at the end. After the third attempt reduced the score by 20% without changing the ranking, I stopped tackling large problems.

## Efficiency5
Someone told me that he solved efficiency13 without much effort, so I started looking at efficiency problems. Using a program to convert ICFP to a JS-compatible format, and throwing it into the web-based prettier made it readable. It seemed to be asking for the smallest Mersenne prime greater than 10^6, so I Googled it and submitted it.

## Efficiency6
Same as above.

## Efficiency12
Same as above, but the program that came out was a mysterious function (factorizes the composite number, then for each prime factor multiplies (p-1)/p and adds 1), so I was ??? in my head but tried it and it worked.

# osak
## First Day

First, I wrote a communication tool that runs in the browser. Since I thought it might be useful later, I also wrote an ICFP interpreter in Rust. However, I got infinitely stuck because I couldn’t properly manage the bindings of the expressions passed to the lambda. It was finished past 6am (the contest started at 9pm in Japan), but by that time, someone had already discovered a technique to use the `echo` command to get ICFP evaluated, so the interpreter turned to be mostly useless.

Lambdaman seemed an approachable code golfing problem. My first thought was it must be Run Length Encoding (a common code golf technique). I created a simple assembler, and by compressing yuusti's DFS solution with RLE in the form of (character)(repeat count), it turned out pretty well. Using that as a base, I continued to make improvements and eventually settled on a string dictionary with N elements and N-based number encoding of payload.

We discussed the idea of creating a path that repeats long patterns, then filling in the gaps at convenient times to achieve the ultimate dictionary compression. However, we couldn’t quite figure out what to search for (though this idea later proved useful for solving the maze). Meanwhile, amylase suggested solving Lambdaman 4 and 5 with a random walk, and our approach quickly shifted.


## Lambdaman 8
Initial solution: The start was DDLLUUUURRRR, and with each loop, DLUR increased by two each. I wrote a naive recursion in the form s1 + s2 + f (DD+s1+LL) (UU+s2+RR). This was around 200B.

Since it didn’t matter if it hit walls, and as long as UR wasn't mixed in during DL, I simplified the recursion to s + (f (DL+s+UR)), which reduced it to about 138B.

Eventually, I realized generating a pattern that passes through the longest part and repeating it would suffice. By using the exponentiation idiom, I eliminated the need for a termination check, shortening it to 116B.

## Lambdaman 16
This was a Hilbert curve. I had never implemented it before, but drawing it out it turned out to follow the recursive pattern below:
  - solve the top left,
  - move slightly down,
  - solve the bottom left,
  - move slightly right,
  - solve the bottom right,
  - move slightly up,
  - solve the top right.

Upon the recursion, the diagonal elements sometimes swapped, sometimes didn’t. This was implemented directly and resulted in 264B. When I came back to shorten it later, I saw that the best solution looked like a RNG solution so gave up.

## Lambdaman 19
A recursive pattern of:
  - Move forward,
  - solve the left-hand side and return,
  - solve the right-hand side and return,
  - solve straight ahead and return,
  - return back.

Naiive implementation resulted in 346B. My initial implementation mistakenly doubled the path length, but it still somehow worked. Since the best solution didn’t seem random, I might have improved it further with more golfing effort.

## Random Numbers
Initial solution: Naive recursion passing the current step count and previous random number, around 160B.

Then I realized that using the random number value for termination instead of the step count would reduce the size to 136B.
Although I thought this involved a probabilistic trick, it turned out (as I learned later) that what I thought was a random number sequence was actually a large cyclic group, making it a genuine approach.

By reducing the number of digits in the constants, the code shrunk further. While discussing this with yuusti, amylase already implemented it.

Recognizing that Lf is equivalent to introducing a local variable, I realized that self-recursion could be done with Lf B$ vf vf, making the Y combinator unnecessarily long. This approach shrunk the code further.

Also noticed that the empty THEN part in 

  "solve lambdamanX " + (IF (end condition) THEN "" ELSE "ULDR"[rand()%4] + (recursion))

seemed wasteful. By reversing the order of recursion, I could save on operations, forming

  (IF (end condition) THEN "solve lambdamanX " ELSE (recursion) + "ULDR"[rand()%4])

which shortened it. Although changing the recursion depth altered the start of the output, making exploration difficult, amylase worked hard to adjust the search. However, since it was a cyclic group, we could have iterated RNG numbers in the reverse order simply by multiplying the inverse element (iwiwi from Unagi told us after the contest).

## Mazes
Although we hadn't found a random sequence that could completely solve it, we had found several setups that could "almost" solve it leaving only tens of cells. I shared the idea with amylase that by inserting strings like UUDD at specific steps during the random walk, we could pass through desired cells without disrupting the random walk. Then, amylase implemented it.

# yuusti
## Lambdaman

After writing a DFS, I was stuck and didn't know what to do next. I thought about doing TSP if I were to be serious about it, but I didn't want to write it. So, I considered if I could solve just the maze part with a simple algorithm and thought about right-hand rule-like methods. However, without feedback from the walls, it seemed impossible.

I thought small patterns might be manageable through repetition. I examined all patterns up to a length of 12 but eventually gave up as it wasn't feasible.

After giving up on Lambdaman, I manually solved Lambdaman and worked on improving small cases for 3D problems.

## 3D1
This involved calculating factorials. The approach was to transform A∗(A−1)+... into 1∗2∗... with hardcoding the checks for A=1 and A=2.

## 3D3
The goal was to determine the sign. There were two approaches: 
- To keep dividing by 2 until it became 1 or -1,
- To compute (A+1)%2 + A%2.

I focused on the former, but the latter turned out to be the correct approach.

For the sake of short coding, I used a trick to overwrite the condition check for A=0 by A=−1 check.

## 3D4
This was about determining the maximum value between A and B. Initially, I incremented A+1 and B+1 separately. By incrementing one by one while swapping A and B, it became more compact.

## 3D5
For calculating the LCM of A and B, I looked at other people's solutions and removed unnecessary TimeWarp operations. By tweaking it, I managed to make it slightly smaller. Key trick was changing the terminal condition of the Euclidean algorithm; originally it was adding 0 to terminate the loop, and I modified it to overwrite an operator that was placed to move away S operator.

