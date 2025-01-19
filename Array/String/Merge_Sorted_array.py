"""
88. Merge Sorted Array
Difficulty: Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

The task is to merge nums1 and nums2 into a single array sorted in non-decreasing order. 
The merged array should be stored inside nums1. 
To accommodate this, nums1 has a length of m + n, where:
- The first m elements represent the elements to merge.
- The last n elements are set to 0 and should be ignored.

nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays to merge are [1,2,3] and [2,5,6].
The merged result is [1,2,2,3,5,6].

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays to merge are [1] and [].
The merged result is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays to merge are [] and [1].
Since m = 0, nums1 contains no elements to merge.

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m is 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n is 0:
            return
        else:
            while m != 0 or n != 0:
                if m != 0 and (nums1[m-1]>=nums2[n-1] or n == 0):
                    nums1[m+n-1]=nums1[m-1]
                    m-=1
                else:
                    print(nums2[n-1])
                    nums1[m+n-1]=nums2[n-1]
                    n-=1
            return