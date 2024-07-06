# 3D1
A loop is necessary, but kindly, the example explains how to create and exit a loop using Time Warp, so I just did the same.

# 3D2
At first, I thought it was impossible without comparisons, but since the input range is small, I tried values from 0 sequentially until it became A or -A. Although a method using A\*sign(A) also emerged, I eventually returned to this solution.

# 3D3
Change 3D2 so that, if the result is root of -A, then \*0-1, or is A, then \*0+1, and if it's 0, then just output 0. On the second day, I woke up and someone had left a brilliant idea that if it’s odd then A%2 is the answer, so I refined that. I didn't realize until the end that it wouldn't die from zero division.

# 3D4
Increment A and B continuously, and when one becomes the other, that's the answer. It was apparently the best solution when arranged neatly.

# 3D5
Just do A\*B/GCD(A, B). It was difficult to avoid division by zero, but it turned out to be unnecessary.

# 3D6
Just try dividing sequentially from 2. The initial code I wrote had a good ranking, so I left it for a long time. However, since the other problems were too difficult, I tweaked it a bit in a few minutes, and it became the best solution.

# 3D7
Consider the n-ary number as a stack, and if it doesn’t change when rearranged, it's a palindrome.

# 3D8
Just loop 3D7, but you need to update the constant 10 you wrote. I devised a subroutine notation (\*\*) to use for updating the values.

(\*\*) Set the period shorter than others, compare input with #, and restore the input to its original value during execution to run once without affecting other programs.

# 3D9
Looking from the end, if ')' comes, add 1, and if '(' comes, subtract 1. If it becomes -1 midway, it's NG. If it ends at 0, it's OK.

# 3D10
Using a stack would have solved it, but initially, I was struggling to update (the stack of consecutive same parentheses, the leading character of the stack), which was a nightmare.

# 3D11
I considered treating the board as memory, but gave up since reading was tough (someone told me it would get TLE anyway because the program was too large). I tried encoding the number of times coordinates were visited from 200\*200 into an integer up to 100^(200\*200), but it TLE'd at the maximum case of 20k steps (limit is 1M steps). When I had the stack of visited coordinates and spent O(N) to avoid duplicate insertion, the integer became up to (200\*200)^100 and it became faster? and it passed. Since the goal was just to pass, I didn't optimize the layout for this one.

# 3D12
At first glance, it looks bad, but just do a Taylor expansion. Initially, I thought no error was allowed and tried various things, but then I realized an error of 1 was acceptable, so I just multiplied by 99 and divided by 99 at the end. After the third attempt reduced the score by 20% without changing the ranking, I stopped tackling large problems.

# Efficiency5
Someone told me that he solved efficiency13 without much effort, so I started looking at efficiency problems. Using a program to convert ICFP to a JS-compatible format, and throwing it into the web-based prettier made it readable. It seemed to be asking for the smallest Mersenne prime greater than 10^6, so I Googled it and submitted it.

# Efficiency6
Same as above.

# Efficiency12
Same as above, but the program that came out was a mysterious function (factorizes the composite number, then for each prime factor multiplies (p-1)/p and adds 1), so I was ??? in my head but tried it and it worked.