'''
114. Flatten Binary Tree to Linked List

Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree, Pre-order Traversal
Companies: Common in technical interviews

Problem Description:
Given the root of a binary tree, flatten the tree into a "linked list" with the following properties:
1. The "linked list" should use the same TreeNode class where:
   - The `right` child pointer points to the next node in the list.
   - The `left` child pointer is always null.
2. The "linked list" should follow the same order as a pre-order traversal of the binary tree.

Examples:

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Explanation:
The tree structure:
       1
      / \
     2   5
    / \    \
   3   4    6
Becomes a flattened "linked list":
1 -> 2 -> 3 -> 4 -> 5 -> 6

Example 2:
Input: root = []
Output: []
Explanation:
An empty tree remains empty after flattening.

Example 3:
Input: root = [0]
Output: [0]
Explanation:
A single-node tree remains the same after flattening.

Constraints:
1. The number of nodes in the tree is in the range [0, 2000].
2. -100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        print("run")
        if not root:
            return root
        lefty = root.left
        righty = root.right
        root.left = None
        if righty:
            self.flatten(righty)
        if lefty:
            self.flatten(lefty)
            temp = root.right
            root.right = lefty
            while lefty.right:
                lefty = lefty.right
            lefty.right = temp
        return root