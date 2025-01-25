'''
226. Invert Binary Tree

Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, invert the tree, and return its root. 
Inverting the tree means swapping the left and right children of all nodes in the tree.

Examples:

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Explanation:
Original Tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9
Inverted Tree:
        4
       / \
      7   2
     / \ / \
    9  6 3  1

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Explanation:
Original Tree:
        2
       / \
      1   3
Inverted Tree:
        2
       / \
      3   1

Example 3:
Input: root = []
Output: []
Explanation:
The tree is empty, so there is no inversion.

Constraints:
1. The number of nodes in the tree is in the range [0, 100].
2. -100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        q = [root]
        while q:
            cNode = q.pop(0)
            left = cNode.left
            right = cNode.right
            cNode.left = None
            cNode.right = None
            if left:
                cNode.right = left
                q.append(left)
            if right:
                cNode.left = right
                q.append(right)
        return root