'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols, and spaces.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        letters = list(s)
        tracker = {}
        present = []
        biggest = 1
        while letters:
            letter = letters.pop()
            if tracker.get(letter,0):
                first = present.pop(0)
                while first != letter:
                    tracker[first] = 0
                    first = present.pop(0)
            else:
                tracker[letter] = 1
            present.append(letter)
            biggest = max(biggest, len(present))
        return biggest