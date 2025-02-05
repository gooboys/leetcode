'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Tree Structure:
      2
     / \
    1   3

Explanation: This is a valid BST because 1 < 2 < 3.

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false

Tree Structure:
      5
     / \
    1   4
       / \
      3   6

Explanation: The tree is invalid because 3 is in the right subtree of 5 but is smaller than 5.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        cur = root
        stack = []
        prev = -2**31-1
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev>=cur.val:
                return False
            prev = cur.val
            cur = cur.right
        return True