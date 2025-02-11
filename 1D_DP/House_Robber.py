'''
198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, but the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected. If two adjacent houses are broken into on the same night, 
it will automatically alert the police.

Given an integer array nums representing the amount of money in each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        prev2 = nums[0]
        prev = nums[1]
        cur = 0
        for i in range(len(nums)-2):
            cur = nums[i+2]
            cur = max(prev2+cur,prev)
            prev2 = max(prev2,prev)
            prev = cur
        return max(prev, prev2)