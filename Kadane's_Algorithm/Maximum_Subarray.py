'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Subarray with the largest sum:
         [-2, 1, -3, **4, -1, 2, 1**, -5, 4]
                         ^^^^^^^^^
Sum = 4 + (-1) + 2 + 1 = 6

Example 2:
Input: nums = [1]
Output: 1

Subarray with the largest sum:
         [**1**]
         ^
Sum = 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Subarray with the largest sum:
         [**5,4,-1,7,8**]
         ^^^^^^^^^^^^^
Sum = 5 + 4 + (-1) + 7 + 8 = 23

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow-up:
- If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -10**4
        tsum = 0
        for i in nums:
            tsum += i
            if tsum>ret:
                ret=tsum
            if tsum<0:
                tsum = 0
        return ret