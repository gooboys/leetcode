"""
189. Rotate Array
Difficulty: Medium

Given an integer array nums, the task is to rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
- Rotate 1 step to the right: [7,1,2,3,4,5,6]
- Rotate 2 steps to the right: [6,7,1,2,3,4,5]
- Rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
- Rotate 1 step to the right: [99,-1,-100,3]
- Rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cp = nums[:]
        size = len(nums)
        diff = k%size
        for i in range(size):
            nums[i] = cp[i-diff]