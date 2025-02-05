'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree and an integer k, return the kth smallest value 
(1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Tree Structure:
      3
     / \
    1   4
     \
      2

Explanation: The in-order traversal of the tree is [1, 2, 3, 4]. The 1st smallest element is 1.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Tree Structure:
        5
       / \
      3   6
     / \
    2   4
   /
  1

Explanation: The in-order traversal of the tree is [1, 2, 3, 4, 5, 6]. The 3rd smallest element is 3.

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        cur = root
        stack = []
        count = 1
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if count == k:
                return cur.val
            count += 1
            cur = cur.right