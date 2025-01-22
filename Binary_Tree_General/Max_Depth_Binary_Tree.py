'''
104. Maximum Depth of Binary Tree

Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given the root of a binary tree, return its maximum depth.

Definition:
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation:
The tree structure:
       3
      / \
     9   20
         / \
        15  7
The longest path from the root to a leaf is 3 -> 20 -> 7, which has a depth of 3.

Example 2:
Input: root = [1,null,2]
Output: 2
Explanation:
The tree structure:
       1
        \
         2
The longest path from the root to a leaf is 1 -> 2, which has a depth of 2.

Constraints:
1. The number of nodes in the tree is in the range [0, 10^4].
2. -100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        q = [root]
        depth = 0
        nodeLoc = {root: 1}
        while q:
            cNode = q.pop(0)
            cDepth = nodeLoc.get(cNode)
            if cDepth > depth:
                depth = cDepth
            cDepth += 1
            if cNode.left:
                nodeLoc[cNode.left] = cDepth
                q.append(cNode.left)
            if cNode.right:
                nodeLoc[cNode.right] = cDepth
                q.append(cNode.right)
        return depth