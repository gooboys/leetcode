'''
42. Trapping Rain Water

Difficulty: Hard
Topics: Array, Two Pointers, Dynamic Programming, Stack
Companies: Common in technical interviews

Problem Description:
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Key Idea:
- Water trapped at a position is determined by the minimum of the maximum heights to its left and right, 
  minus its own height.

Examples:

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation:
- The elevation map is represented by the array [0,1,0,2,1,0,1,3,2,1,2,1].
- The trapped rainwater (blue sections) adds up to 6 units.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Explanation:
- The trapped rainwater adds up to 9 units.

Constraints:
1. `n == height.length`
2. 1 <= n <= 2 * 10^4
3. 0 <= height[i] <= 10^5
'''



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        prevAdd = 0
        lasthigh = 0
        lasthighIndex = 0
        size = len(height)
        for i in range(size):
            if lasthigh<=height[i]:
                lasthigh = height[i]
                ret += prevAdd
                prevAdd = 0 
                lasthighIndex = i
            else:
                prevAdd += lasthigh - height[i]
        prevAdd = 0
        lasthigh = 0
        for i in range(size-lasthighIndex):
            if lasthigh<=height[size-i-1]:
                lasthigh = height[size-i-1]
                ret += prevAdd
                prevAdd = 0
            else:
                prevAdd += lasthigh - height[size-i-1]
        return ret
            