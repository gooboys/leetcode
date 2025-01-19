"""
26. Remove Duplicates from Sorted Array
Difficulty: Easy

Given an integer array nums sorted in non-decreasing order, the task is to remove duplicates in-place such that 
each unique element appears only once. The relative order of the elements must be maintained. 
Return the number of unique elements in nums.

The function must achieve the following:
1. Modify nums such that the first k elements contain the unique elements in the same order as they appear in nums.
2. The remaining elements in nums are not important.
3. Return k, the number of unique elements.

Custom Judge:
The solution will be tested with the following process:
- Initialize nums (input array) and expectedNums (correct result with length k).
- Ensure the first k elements of nums match the expectedNums array after calling the function.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: The function should return k = 2, with the first two elements of nums being 1 and 2. 
The remaining elements are not important.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: The function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4. 
The remaining elements are not important.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -101
        count = 0
        for i in nums:
            if i != ret:
                nums[count] = i
                count += 1
                ret = i
        return count