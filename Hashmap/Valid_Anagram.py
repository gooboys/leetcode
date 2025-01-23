'''
242. Valid Anagram

Difficulty: Easy
Topics: Hash Table, String, Sorting
Companies: Common in technical interviews

Problem Description:
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

Definition:
An anagram is a word or phrase formed by rearranging the letters of another, 
using all the original letters exactly once.

Examples:

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True
Explanation:
- The string "t" can be formed by rearranging the letters of "s".

Example 2:
Input: s = "rat", t = "car"
Output: False
Explanation:
- The string "t" cannot be formed by rearranging the letters of "s".

Constraints:
1. 1 <= s.length, t.length <= 5 * 10^4
2. `s` and `t` consist of lowercase English letters.
'''



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ret = {}
        for i in s:
            ret[i] = ret.get(i,0) + 1
        for i in t:
            if ret.get(i,0) == 0:
                return False
            ret[i] = ret[i] - 1
        if sum(ret.values()) == 0:
            return True
        else:
            return False