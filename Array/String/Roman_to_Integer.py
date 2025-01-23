'''
13. Roman to Integer

Difficulty: Easy
Topics: String, Hash Table
Companies: Common in technical interviews

Problem Description:
Roman numerals are represented by seven different symbols with the following values:

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Key Notes:
1. Roman numerals are usually written largest to smallest from left to right.
   - Example: 2 is written as II (1 + 1), 12 is written as XII (10 + 1 + 1), and 27 is XXVII (10 + 10 + 5 + 1 + 1).
2. There are six instances where subtraction is used:
   - I can be placed before V (5) and X (10) to make 4 and 9.
   - X can be placed before L (50) and C (100) to make 40 and 90.
   - C can be placed before D (500) and M (1000) to make 400 and 900.

Task:
Given a Roman numeral string `s`, convert it to an integer.

Examples:

Example 1:
Input: s = "III"
Output: 3
Explanation:
- III = 3 (1 + 1 + 1).

Example 2:
Input: s = "LVIII"
Output: 58
Explanation:
- L = 50, V = 5, III = 3 (50 + 5 + 3).

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation:
- M = 1000, CM = 900, XC = 90, IV = 4 (1000 + 900 + 90 + 4).

Constraints:
1. 1 <= s.length <= 15
2. `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
3. It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999].
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        chars = {
            'M':1000, 'CM':900, 'D':500, 'CD': 400,
            'C':100, 'XC':90, 'L':50, 'XL':40,
            'X':10, 'IX':9, 'V':5, 'IV':4, 'I': 1
        }
        for i in range(len(s)-1):
            double = chars.get(s[i]+s[i+1],0)
            if double:
                total += double
                total -= chars.get(s[i+1],0)
            else:
                total += chars.get(s[i])
        total += chars[s[-1]]
        return total