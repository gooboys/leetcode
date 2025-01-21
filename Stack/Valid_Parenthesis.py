'''
20. Valid Parentheses

Difficulty: Easy
Topics: Stack, String
Companies: Common in technical interviews

Problem Description:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket must have a corresponding open bracket of the same type.

Examples:

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([])"
Output: True

Constraints:
1. 1 <= s.length <= 10^4
2. `s` consists only of parentheses characters: '()', '[]', and '{}'.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tracker = []
        for i in s:
            if i == '{' or i == '[' or i == '(':
                tracker.append(i)
            elif len(tracker) == 0:
                return False
            elif i == ')':
                if tracker[-1] == '(':
                    tracker.pop()
                else:
                    return False
            elif i == '}':
                if tracker[-1] == '{':
                    tracker.pop()
                else:
                    return False
            elif i == ']':
                if tracker[-1] == '[':
                    tracker.pop()
                else:
                    return False
        if len(tracker) == 0:
            return True
        else:
            return False