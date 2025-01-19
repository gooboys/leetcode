"""
27. Remove Element
Difficulty: Easy

Given an integer array nums and an integer val, the task is to remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Return the number of elements in nums that are not equal to val.

The function must achieve the following:
1. Modify nums such that the first k elements of nums contain the elements not equal to val.
2. The remaining elements of nums are not important.
3. Return k, the number of elements not equal to val.

Custom Judge:
The solution will be tested with the following process:
- Initialize nums (input array) and val (value to remove).
- Calculate the expectedNums array (correct result with length k).
- Ensure the first k elements of nums match the expectedNums array after calling the function.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: The function should return k = 2, with the first two elements of nums being 2. 
The remaining elements are not important.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: The function should return k = 5, with the first five elements of nums being 0, 1, 4, 0, and 3.
The remaining elements are not important.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
        return count