"""
80. Remove Duplicates from Sorted Array II
Difficulty: Medium

Given an integer array nums sorted in non-decreasing order, the task is to remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements must be maintained.

Requirements:
1. Modify nums such that the first k elements contain the final result after removing duplicates.
2. The remaining elements in nums are not important.
3. Return k, the number of elements in the modified array.

Constraints:
- Do not allocate extra space for another array.
- Use O(1) extra memory.

Custom Judge:
The solution will be tested with the following process:
- Initialize nums (input array) and expectedNums (correct result with length k).
- Ensure the first k elements of nums match the expectedNums array after calling the function.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: The function should return k = 5, with the first five elements of nums being 1, 1, 2, 2, and 3. 
The remaining elements are not important.

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: The function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3, and 3. 
The remaining elements are not important.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        prev = -10001
        tempcount = 0
        for i in nums:
            if i != prev:
                nums[index] = i
                tempcount = 1
                index += 1
                prev = i
            elif tempcount == 1:
                nums[index] = i
                index += 1
                tempcount += 1
        return index