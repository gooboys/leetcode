'''
172. Factorial Trailing Zeroes

Difficulty: Medium
Topics: Math
Companies: Common in technical interviews

Problem Description:
Given an integer `n`, return the number of trailing zeroes in `n!` (n factorial).

Definition:
n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

Key Insight:
Trailing zeroes in a factorial are caused by the factors of 10 in the product. Since 10 = 2 * 5, and there are usually more factors of 2 than 5 in factorials, the number of trailing zeroes is determined by the number of factors of 5 in `n!`.

Examples:

Example 1:
Input: n = 3
Output: 0
Explanation:
3! = 6, which has no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation:
5! = 120, which has one trailing zero.

Example 3:
Input: n = 0
Output: 0
Explanation:
0! = 1, which has no trailing zero.

Constraints:
1. 0 <= n <= 10^4
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        total = 1
        for i in range(n):
            total *= i+1
        string = str(total)
        string = string[::-1]
        ret = 0
        for i in string:
            if i == '0':
                ret += 1
            else:
                return ret
