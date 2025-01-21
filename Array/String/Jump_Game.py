'''
55. Jump Game

Difficulty: Medium
Topics: Arrays, Greedy Algorithm
Companies: Common in technical interviews

Problem Description:
You are given an integer array `nums`. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Objective:
Return `True` if you can reach the last index, or `False` otherwise.

Examples:

Example 1:
Input: nums = [2,3,1,1,4]
Output: True
Explanation: 
- Jump 1 step from index 0 to 1. 
- Then jump 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: False
Explanation: 
- You will always arrive at index 3 no matter what.
- Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1. 1 <= nums.length <= 10^4
2. 0 <= nums[i] <= 10^5
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.reverse()
        distance = 0
        ret = False
        for i in nums:
            if distance<=i:
                distance = 0
                ret = True
            else:
                ret = False
            distance += 1
        return ret