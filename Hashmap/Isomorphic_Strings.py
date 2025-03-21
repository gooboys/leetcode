"""
205. Isomorphic Strings
Difficulty: Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t. 
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
- 'e' maps to 'a', and 'g' maps to 'd'.
- The strings can be made identical through these mappings.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
- 'o' would need to map to both 'a' and 'r', which is not allowed.

Example 3:
Input: s = "paper", t = "title"
Output: true
Explanation:
- 'p' maps to 't', 'a' maps to 'i', 'p' maps to 't', 'e' maps to 'l', and 'r' maps to 'e'.
- The strings can be made identical through these mappings.

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ASCII characters.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        both = zip(s,t)
        tracker = {}
        track = {}
        for first, second in both:
            temp = tracker.get(first,0)
            tempy = track.get(second,0)
            print(temp,tempy)
            if temp == 0 and tempy == 0:
                tracker[first] = second
                track[second] = first
            elif temp != second or tempy != first:
                return False
        return True