'''
70. Climbing Stairs

Difficulty: Easy
Topics: Dynamic Programming, Recursion, Math
Companies: Common in technical interviews

Problem Description:
You are climbing a staircase. It takes `n` steps to reach the top.

Rules:
- Each time you can climb either 1 step or 2 steps.
- Determine the number of distinct ways you can climb to the top.

Examples:

Example 1:
Input: n = 2
Output: 2
Explanation:
There are two distinct ways to climb to the top:
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation:
There are three distinct ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1. 1 <= n <= 45
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        values = [1,2]
        for i in range(n-2):
            values.append(values[i]+values[i+1])
        return values[-1]