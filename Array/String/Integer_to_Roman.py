'''
12. Integer to Roman

Difficulty: Medium
Topics: Math, String
Companies: Common in technical interviews

Problem Description:
Seven different symbols represent Roman numerals with the following values:

Symbol    Value
I         1
V         5
X         10
L         50
C         100
D         500
M         1000

Rules for converting a decimal number to a Roman numeral:
1. Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
2. Conversion rules:
   - If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder.
   - If the value starts with 4 or 9, use the subtractive form, for example:
       - 4 is represented as IV (1 less than 5).
       - 9 is represented as IX (1 less than 10).
       - Other subtractive forms include 40 (XL), 90 (XC), 400 (CD), and 900 (CM).
   - Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times.
   - If you need to append a symbol 4 times, use the subtractive form instead.

Task:
Given an integer, convert it to a Roman numeral.

Examples:

Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
- 3000 = MMM (M + M + M)
- 700 = DCC (D + C + C)
- 40 = XL (X less than L)
- 9 = IX (I less than X)

Example 2:
Input: num = 58
Output: "LVIII"
Explanation:
- 50 = L
- 8 = VIII

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation:
- 1000 = M
- 900 = CM (C less than M)
- 90 = XC (X less than C)
- 4 = IV (I less than V)

Constraints:
1. 1 <= num <= 3999
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        integers = [-1]*4
        string = str(num)
        string = string[::-1]
        for i in range(len(string)):
            integers[3-i] = int(string[i])
        ones = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
        tens = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
        huns = {0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
        thous = {0:'',1:'M',2:'MM',3:'MMM'}
        if integers[0] != -1:
            ret += thous[integers[0]]
        if integers[1] != -1:
            ret += huns[integers[1]]
        if integers[2] != -1:
            ret += tens[integers[2]]
        if integers[3] != -1:
            ret += ones[integers[3]]
        return ret