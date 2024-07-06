# Efficiency

- When I looked at the code, it was creating recursive functions using a fixed-point combinator.
- Problems 7 and 8 boil down to something like "find the smallest x that satisfies the logical expressions between each bit (many of them)," so they can be solved using a SAT solver.
- While the above was dealing with the relationships of each digit in binary, problems 9 to 11 solve logical expressions for each digit in base-9. This becomes a 9-coloring problem (I later heard it was like Sudoku), so I used an LP solver.
