"""
290. Word Pattern
Difficulty: Easy

Given a pattern and a string s, determine if s follows the same pattern.

A match is defined as a full bijection between a letter in the pattern and a non-empty word in s:
1. Each letter in the pattern maps to exactly one unique word in s.
2. Each unique word in s maps to exactly one letter in the pattern.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
- 'a' maps to "dog".
- 'b' maps to "cat".
- This mapping satisfies the bijection.

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Explanation:
- The mapping fails because "fish" cannot map to 'b' when "cat" already maps to it.

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Explanation:
- The mapping fails because all 'a's would need to map to the same word, but they map to different ones.

Constraints:
- 1 <= pattern.length <= 300
- pattern contains only lowercase English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain leading or trailing spaces.
- All words in s are separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        full = zip(words,pattern)
        if len(words) != len(pattern):
            return False
        for x, y in full:
            if words.index(x) != pattern.index(y):
                return False
        return True