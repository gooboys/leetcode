'''
9. Palindrome Number

Difficulty: Easy
Topics: Math, Two-Pointer
Companies: Common in technical interviews

Problem Description:
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

Definition:
An integer is a palindrome when it reads the same backward as forward.

Examples:

Example 1:
Input: x = 121
Output: True
Explanation:
121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: False
Explanation:
From left to right, it reads -121.
From right to left, it becomes 121-, which is not a palindrome.

Example 3:
Input: x = 10
Output: False
Explanation:
Reads 01 from right to left, which is not the same as 10.

Constraints:
1. -2^31 <= x <= 2^31 - 1
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        for i in range(len(string)):
            if string[i] != string[-1* (i+1)]:
                return False
        return True