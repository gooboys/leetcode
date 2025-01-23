'''
49. Group Anagrams

Difficulty: Medium
Topics: Hash Table, String, Sorting
Companies: Common in technical interviews

Problem Description:
Given an array of strings `strs`, group the anagrams together. 
You can return the answer in any order.

Definition:
An anagram is a word or phrase formed by rearranging the letters of another, 
using all the original letters exactly once.

Examples:

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- "bat" has no other anagrams.
- "nat" and "tan" are anagrams as they can be rearranged to form each other.
- "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]
Explanation:
- A single empty string is its own group.

Example 3:
Input: strs = ["a"]
Output: [["a"]]
Explanation:
- A single character is its own group.

Constraints:
1. 1 <= strs.length <= 10^4
2. 0 <= strs[i].length <= 100
3. `strs[i]` consists of lowercase English letters.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        dicts = []
        if len(strs)==1:
            return [strs]
        while strs:
            cWord = strs.pop(0)
            tempdict = {}
            for i in cWord:
                tempdict[i] = tempdict.get(i,0) + 1
            notAdded = True
            for i in range(len(ret)):
                if tempdict == dicts[i]:
                    ret[i].append(cWord)
                    notAdded = False
            if notAdded:
                ret.append([cWord])
                dicts.append(tempdict)
        return ret