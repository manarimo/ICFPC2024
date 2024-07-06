# Lambdaman

Using one character for each of LRDU is clearly inefficient, so I considered encoding. On the first day, I managed to come up with a fairly effective encoding that was reasonably short.

After that, I had no new ideas and stalled for over a day. As answers exceeding the theoretical limits of information theory appeared in the rankings, I realized that the compression approach would never win, so I started over. On Sunday night, I finally came up with the idea of a random walk. Although my team members were quite skeptical, trying it out was quick, and when I managed to solve lambdaman4, I was convinced this was the solution.

For the random number generation used in the random walk, I chose the linear congruential method because it’s simple to implement. When looking up coefficients on Wikipedia, I found a setting without a constant term: next = (48271 * x) % (2 << 31 - 1), which was advantageous for code golfing, so I adopted it.

Upon reflection, I realized this worked because the modulus is a (Mersenne) prime and 48271 is likely a primitive root, thus maximizing the period. I discovered that if the parameters meet the same conditions, smaller ones would result in shorter code. Then, I just wrote the program and ran it. Specific generator code was shrunk significantly by osak’s exceptional code golfing, so I’m not entirely sure about the details.


# Efficiency
- 1: When the source code is executed, it obviously doesn’t stop, but reading the code shows it’s applying a quadrupling operation 22 times.
- 2: I found that a large loop was running but multiplying the result by 0. At this point, I realized it was a game of code reading.

I read through several more, but didn’t solve some myself, such as problems 7-11 which used a SAT solver.