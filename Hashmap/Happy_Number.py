'''
202. Happy Number

Difficulty: Easy
Topics: Math, Hash Table, Two Pointers
Companies: Common in technical interviews

Problem Description:
Write an algorithm to determine if a number `n` is happy.

Definition:
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Numbers for which this process ends in 1 are happy numbers.

Return `True` if `n` is a happy number, and `False` if not.

Examples:

Example 1:
Input: n = 19
Output: True
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: False
Explanation:
The process enters a cycle and does not reach 1.

Constraints:
1. 1 <= n <= 2^31 - 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        string = ""
        tracker = {}
        while n != 1:
            string = str(n)
            n = 0
            for i in string:
                n += int(i) ** 2
            if tracker.get(n,0) == 0:
                tracker[n] = 1
            else:
                return False
        return True