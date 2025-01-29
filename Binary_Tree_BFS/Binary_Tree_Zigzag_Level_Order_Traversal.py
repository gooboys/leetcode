'''
103. Binary Tree Zigzag Level Order Traversal

Difficulty: Medium
Topics: Tree, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. 
Zigzag traversal alternates the order of traversal between levels:
- Left-to-right for one level, then right-to-left for the next, and so on.

Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Explanation:
- Level 0: [3]
- Level 1: [20,9] (right-to-left)
- Level 2: [15,7] (left-to-right)

Example 2:
Input: root = [1]
Output: [[1]]
Explanation:
- The tree has only one node, so the traversal is [[1]].

Example 3:
Input: root = []
Output: []
Explanation:
- The tree is empty, so the traversal is an empty list.

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
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        ret = []
        forward = True
        while q:
            tList = []
            for _ in range(len(q)):
                cNode = q.pop(0)
                tList.append(cNode.val)
                if cNode.right:
                    q.append(cNode.right)
                if cNode.left:
                    q.append(cNode.left)
            if forward:
                tList.reverse()
            forward = not forward
            ret.append(tList)
        return ret