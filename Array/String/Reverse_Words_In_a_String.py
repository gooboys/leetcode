'''
151. Reverse Words in a String

Difficulty: Medium
Topics: String, Two Pointers
Companies: Common in technical interviews

Problem Description:
Given an input string `s`, reverse the order of the words.

Definitions:
1. A word is defined as a sequence of non-space characters.
2. Words in `s` are separated by at least one space.

Task:
Return a string of the words in reverse order, concatenated by a single space.
- The returned string should only have a single space separating the words.
- Do not include any extra spaces, even if the input string has leading or trailing spaces or multiple spaces between words.

Examples:

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
Explanation:
- Reverse the order of the words.

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation:
- Trim leading and trailing spaces.
- Reverse the order of the words.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation:
- Reduce multiple spaces between words to a single space.
- Reverse the order of the words.

Constraints:
1. 1 <= s.length <= 10^4
2. `s` contains English letters (upper-case and lower-case), digits, and spaces (' ').
3. There is at least one word in `s`.
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split = s.split(' ')
        split.reverse()
        ret = ""
        for i in split:
            if i != '':
                ret += i+" "
        ret = ret[:-1]
        return ret