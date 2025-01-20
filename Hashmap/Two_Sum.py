"""
1. Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Assumptions:
1. Each input has exactly one solution.
2. You may not use the same element twice.
3. The answer can be returned in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation:
- nums[0] + nums[1] = 2 + 7 = 9.
- Return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation:
- nums[1] + nums[2] = 2 + 4 = 6.
- Return [1, 2].

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Explanation:
- nums[0] + nums[1] = 3 + 3 = 6.
- Return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = {}
        for i in range(len(nums)):
            if ret.get(nums[i], 'a') != 'a':
                return [ret[nums[i]], i]
            temp = target - nums[i]
            ret[temp] = i