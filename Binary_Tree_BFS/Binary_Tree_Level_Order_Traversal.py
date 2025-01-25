'''
102. Binary Tree Level Order Traversal

Difficulty: Medium
Topics: Tree, Breadth-First Search (BFS)
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, return the level order traversal of its nodes' values. 
This means traversing the tree level by level from left to right.

Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation:
- Level 0: [3]
- Level 1: [9,20]
- Level 2: [15,7]

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
2. -1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            qLen = len(queue)
            tempList = []
            for i in range(qLen):
                cNode = queue.pop(0)
                tempList.append(cNode.val)
                if cNode.left:
                    queue.append(cNode.left)
                if cNode.right:
                    queue.append(cNode.right)
            ret.append(tempList)
        return ret