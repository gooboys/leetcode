'''
100. Same Tree

Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Definition:
Two binary trees are considered the same if:
1. They are structurally identical.
2. The nodes have the same values.

Examples:

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: True
Explanation:
Both trees have the same structure and node values:
    1          1
   / \        / \
  2   3      2   3

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: False
Explanation:
The trees have different structures:
    1          1
   /            \
  2              2

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: False
Explanation:
The trees have the same structure but different node values:
    1          1
   / \        / \
  2   1      1   2

Constraints:
1. The number of nodes in both trees is in the range [0, 100].
2. -10^4 <= Node.val <= 10^4
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        lefty = self.isSameTree(p.left,q.left)
        righty = self.isSameTree(p.right,q.right)
        return lefty and righty