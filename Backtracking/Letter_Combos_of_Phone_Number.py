"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        digits = list(digits)
        ref = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ret = []
        if len(digits) == 1:
            return ref[digits[0]]
        elif len(digits) == 2:
            for letter1 in ref[digits[0]]:
                for letter2 in ref[digits[1]]:
                    ret.append(letter1+letter2)
        elif len(digits) == 3:
            for letter1 in ref[digits[0]]:
                for letter2 in ref[digits[1]]:
                    for letter3 in ref[digits[2]]:
                        ret.append(letter1+letter2+letter3)
        else:
            for letter1 in ref[digits[0]]:
                for letter2 in ref[digits[1]]:
                    for letter3 in ref[digits[2]]:
                        for letter4 in ref[digits[3]]:
                            ret.append(letter1+letter2+letter3+letter4)
        return ret
