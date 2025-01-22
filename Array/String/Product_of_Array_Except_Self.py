'''
238. Product of Array Except Self

Difficulty: Medium
Topics: Array, Prefix Sum
Companies: Common in technical interviews

Problem Description:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Constraints:
1. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
2. You must write an algorithm that runs in O(n) time.
3. You cannot use the division operation.

Examples:

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
- For index 0: The product of elements except 1 is 2 * 3 * 4 = 24.
- For index 1: The product of elements except 2 is 1 * 3 * 4 = 12.
- For index 2: The product of elements except 3 is 1 * 2 * 4 = 8.
- For index 3: The product of elements except 4 is 1 * 2 * 3 = 6.

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation:
- For index 0: The product of elements except -1 is 1 * 0 * -3 * 3 = 0.
- For index 1: The product of elements except 1 is -1 * 0 * -3 * 3 = 0.
- For index 2: The product of elements except 0 is -1 * 1 * -3 * 3 = 9.
- For index 3: The product of elements except -3 is -1 * 1 * 0 * 3 = 0.
- For index 4: The product of elements except 3 is -1 * 1 * 0 * -3 = 0.

Constraints:
1. 2 <= nums.length <= 10^5
2. -30 <= nums[i] <= 30
3. The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.
'''



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        forward = [0]*size
        backward = [0]*size
        ret = [0]*size
        count = 1
        for i in range(size):
            count*=nums[i]
            forward[i] = count
        nums.reverse()
        count = 1
        for i in range(size):
            count*=nums[i]
            backward[i] = count
        backward.reverse()
        for i in range(size-2):
            fill = forward[i]*backward[i+2]
            ret[i+1] = fill
        ret[0] = backward[1]
        ret[-1] = forward[-2]
        return ret