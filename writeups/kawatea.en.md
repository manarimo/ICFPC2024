# Spaceship

Since there were no walls or winds like in the AtCoder Masters Final (https://atcoder.jp/contests/masters2024-final), I wrote a greedy algorithm to move precisely to the next vertex.

Upon re-reading the problem statement, I realized the order was not fixed, so I sorted the input by coordinates.

To further improve the order, I solved the TSP using the distance from the greedy method as the cost.

By playing around with small problems by hand to gain better insights, I noticed that many problems could be solved by filling in gaps in the order, if the order was set well.

For the TSP order, I wrote a beam search that considered the state as the vertices visited and the current speed, with transitions to the next vertex. The movement commands were exhaustively searched up to about five moves.

I also tried a version that didn’t fix the visiting order and flagged the visited vertices, but it didn’t make much difference.

For larger problems with greater distances between vertices that couldn't be solved this way, I wrote another beam search treating each transition as a single command.

For some problems where the best solution wasn’t quite reached, the TSP order didn’t seem optimal, so I wrote simulated annealing to slightly change the order. The transitions for the annealing included moving one vertex to another place, moving a continuous section of vertices to another place, and reversing a continuous section of vertices.

I kept tweaking the parameters of the beam search and simulated annealing, running them repeatedly.
