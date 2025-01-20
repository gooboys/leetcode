"""
125. Valid Palindrome
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation:
- After removing non-alphanumeric characters and converting to lowercase, s becomes "amanaplanacanalpanama".
- This reads the same forward and backward, so it is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation:
- After processing, s becomes "raceacar".
- This does not read the same forward and backward, so it is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation:
- After processing, s becomes an empty string "".
- An empty string is considered a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaner = ""
        for char in s:
            if char.isalnum():
                cleaner += char.lower()
        for i in range(len(cleaner)):
            if cleaner[i] != cleaner[-1*(i+1)]:
                return False
        return True