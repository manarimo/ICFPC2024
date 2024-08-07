# First Day

First, I wrote a communication tool that runs in the browser. Since I thought it might be useful later, I also wrote an ICFP interpreter in Rust. However, I got infinitely stuck because I couldn’t properly manage the bindings of the expressions passed to the lambda. It was finished past 6am (the contest started at 9pm in Japan), but by that time, someone had already discovered a technique to use the `echo` command to get ICFP evaluated, so the interpreter turned to be mostly useless.

Lambdaman seemed an approachable code golfing problem. My first thought was it must be Run Length Encoding (a common code golf technique). I created a simple assembler, and by compressing yuusti's DFS solution with RLE in the form of (character)(repeat count), it turned out pretty well. Using that as a base, I continued to make improvements and eventually settled on a string dictionary with N elements and N-based number encoding of payload.

We discussed the idea of creating a path that repeats long patterns, then filling in the gaps at convenient times to achieve the ultimate dictionary compression. However, we couldn’t quite figure out what to search for (though this idea later proved useful for solving the maze). Meanwhile, amylase suggested solving Lambdaman 4 and 5 with a random walk, and our approach quickly shifted.


# Lambdaman 8
Initial solution: The start was DDLLUUUURRRR, and with each loop, DLUR increased by two each. I wrote a naive recursion in the form s1 + s2 + f (DD+s1+LL) (UU+s2+RR). This was around 200B.

Since it didn’t matter if it hit walls, and as long as UR wasn't mixed in during DL, I simplified the recursion to s + (f (DL+s+UR)), which reduced it to about 138B.

Eventually, I realized generating a pattern that passes through the longest part and repeating it would suffice. By using the exponentiation idiom, I eliminated the need for a termination check, shortening it to 116B.

# Lambdaman 16
This was a Hilbert curve. I had never implemented it before, but drawing it out it turned out to follow the recursive pattern below:
  - solve the top left,
  - move slightly down,
  - solve the bottom left,
  - move slightly right,
  - solve the bottom right,
  - move slightly up,
  - solve the top right.

Upon the recursion, the diagonal elements sometimes swapped, sometimes didn’t. This was implemented directly and resulted in 264B. When I came back to shorten it later, I saw that the best solution looked like a RNG solution so gave up.

# Lambdaman 19
A recursive pattern of:
  - Move forward,
  - solve the left-hand side and return,
  - solve the right-hand side and return,
  - solve straight ahead and return,
  - return back.

Naiive implementation resulted in 346B. My initial implementation mistakenly doubled the path length, but it still somehow worked. Since the best solution didn’t seem random, I might have improved it further with more golfing effort.

# Random Numbers
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

# Mazes
Although we hadn't found a random sequence that could completely solve it, we had found several setups that could "almost" solve it leaving only tens of cells. I shared the idea with amylase that by inserting strings like UUDD at specific steps during the random walk, we could pass through desired cells without disrupting the random walk. Then, amylase implemented it.
