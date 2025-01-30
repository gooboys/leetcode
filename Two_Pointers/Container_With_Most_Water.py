'''
11. Container With Most Water

Difficulty: Medium
Topics: Array, Two Pointers, Greedy
Companies: Common in technical interviews

Problem Description:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that:
- The two endpoints of the `i-th` line are at coordinates `(i, 0)` and `(i, height[i])`.

Task:
Find two lines that, together with the x-axis, form a container that holds the most water.
Return the **maximum amount of water** that the container can store.

Key Constraints:
- The container **cannot be slanted**, meaning the water level is determined by the shorter line.

Examples:

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
- The maximum area is formed by the lines at index 1 and 8.
- Area = min(8,7) * (8 - 1) = 7 * 7 = 49.

Example 2:
Input: height = [1,1]
Output: 1
Explanation:
- The only possible container is formed by the two lines, storing 1 unit of water.

Constraints:
1. `n == height.length`
2. `2 <= n <= 10^5`
3. `0 <= height[i] <= 10^4`
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        ret = 0
        while left != right:
            lefty = height[left]
            righty = height[right]
            tempVal = min(lefty,righty)*(right-left)
            if tempVal > ret:
                ret = tempVal
            if lefty>righty:
                right -= 1
            else:
                left += 1
        return ret