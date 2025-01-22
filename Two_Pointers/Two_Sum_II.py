'''
167. Two Sum II - Input Array Is Sorted

Difficulty: Medium
Topics: Two Pointers, Binary Search, Array
Companies: Common in technical interviews

Problem Description:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.

Task:
- Let these two numbers be `numbers[index1]` and `numbers[index2]` where 1 <= index1 < index2 <= numbers.length.
- Return the indices of the two numbers as an integer array `[index1, index2]` of length 2.
- The returned indices must be 1-indexed.
- You may not use the same element twice.

Key Constraints:
1. Your solution must use only constant extra space.

Examples:

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation:
- The sum of 2 and 7 is 9. 
- Therefore, index1 = 1, index2 = 2. 
- We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation:
- The sum of 2 and 4 is 6. 
- Therefore, index1 = 1, index2 = 3. 
- We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation:
- The sum of -1 and 0 is -1. 
- Therefore, index1 = 1, index2 = 2. 
- We return [1, 2].

Constraints:
1. 2 <= numbers.length <= 3 * 10^4
2. -1000 <= numbers[i] <= 1000
3. `numbers` is sorted in non-decreasing order.
4. -1000 <= target <= 1000
5. The tests are generated such that there is exactly one solution.
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1 = 0
        p2 = len(numbers)-1
        while p1<p2:
            total = numbers[p1] + numbers[p2]
            if total>target:
                p2-=1
            elif total<target:
                p1+=1
            else:
                return [p1+1,p2+1]