'''
274. H-Index

Difficulty: Medium
Topics: Array, Sorting
Companies: Common in technical interviews

Problem Description:
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

Definition:
According to the definition of h-index on Wikipedia:
- The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers 
  that have each been cited at least `h` times.

Examples:

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation:
- The researcher has 5 papers with citations [3, 0, 6, 1, 5].
- They have 3 papers with at least 3 citations each, and the remaining two papers have no more than 3 citations each.
- Therefore, the h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
Explanation:
- The researcher has 1 paper with at least 1 citation, and the other two papers have no more than 1 citation.
- Therefore, the h-index is 1.

Constraints:
1. n == citations.length
2. 1 <= n <= 5000
3. 0 <= citations[i] <= 1000
'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 1 and citations[0]>0:
            return 1
        elif len(citations) == 1:
            return 0
        citations.sort()
        citations.reverse()
        mid = 0
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)