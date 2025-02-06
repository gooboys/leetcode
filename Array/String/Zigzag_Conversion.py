'''
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

For numRows = 3:
P   A   H   N
A P L S I I G
Y   I   R

Read line by line: "PAHNAPLSIIGYIR"

Write a function that converts a given string into a zigzag pattern and then reads it row by row.

Function signature:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Zigzag Pattern:
P   A   H   N
A P L S I I G
Y   I   R

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Zigzag Pattern:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows>=len(s):
            return s
        if numRows == 1:
            return s
        indices = len(s)
        curChar = 0
        curRow = 0
        tracker = {}
        down = True
        while curChar<indices:
            tracker[curRow] = tracker.get(curRow, "") + s[curChar]
            print(s[curChar])
            curChar += 1
            if curRow == 0:
                down = True
            elif curRow == numRows-1:
                down = False
            if down:
                curRow += 1
            else:
                curRow -= 1
        ret = ""
        for i in range(numRows):
            ret += tracker[i]
        return ret