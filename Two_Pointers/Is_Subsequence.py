'''
392. Is Subsequence

Difficulty: Easy
Topics: Two Pointers, String
Companies: Common in technical interviews

Problem Description:
Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`, or `False` otherwise.

Definition:
A subsequence of a string is a new string formed from the original string by deleting some (or none) of the characters without disturbing the relative positions of the remaining characters. 
Example: "ace" is a subsequence of "abcde", but "aec" is not.

Examples:

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: True
Explanation:
- "abc" can be formed by deleting 'h', 'b', 'g', and 'd' from "ahbgdc".

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: False
Explanation:
- "axc" cannot be formed from "ahbgdc" as 'x' is missing.

Constraints:
1. 0 <= s.length <= 100
2. 0 <= t.length <= 10^4
3. `s` and `t` consist only of lowercase English letters.
'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len1 = len(s)
        len2 = len(t)
        p1 = 0
        p2 = 0
        while p1 != len1 and p2 != len2:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        if p1 != len1:
            return False
        else:
            return True
        