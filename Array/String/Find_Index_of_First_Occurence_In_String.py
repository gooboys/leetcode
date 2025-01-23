'''
28. Find the Index of the First Occurrence in a String

Difficulty: Easy
Topics: String, Two Pointers
Companies: Common in technical interviews

Problem Description:
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Examples:

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation:
- "sad" occurs at index 0 and 6 in "sadbutsad".
- The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation:
- "leeto" does not occur in "leetcode", so we return -1.

Constraints:
1. 1 <= haystack.length, needle.length <= 10^4
2. `haystack` and `needle` consist of only lowercase English characters.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)