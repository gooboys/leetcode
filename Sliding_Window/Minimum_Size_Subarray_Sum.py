'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
'''


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] >= target:
            return 1
        length = 10**5
        tSum = nums[0]
        right = 0
        left = 0
        while True:
            if tSum<target:
                if right == len(nums)-1:
                    break
                right += 1
                tSum += nums[right]
            else:
                length = min(length, right-left)
                tSum -= nums[left]
                left += 1
        if length == 10**5:
            return 0
        return length+1