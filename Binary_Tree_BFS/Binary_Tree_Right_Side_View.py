'''
199. Binary Tree Right Side View

Difficulty: Medium
Topics: Tree, Breadth-First Search, Depth-First Search
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, imagine yourself standing on the right side of it. 
Return the values of the nodes you can see, ordered from top to bottom.

Examples:

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:
- Standing on the right side, you see nodes 1, 3, and 4.

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:
- Standing on the right side, you see nodes 1, 3, 4, and 5.

Example 3:
Input: root = [1,null,3]
Output: [1,3]
Explanation:
- Standing on the right side, you see nodes 1 and 3.

Example 4:
Input: root = []
Output: []
Explanation:
- The tree is empty, so no nodes are visible.

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
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        q = [root,None]
        ret = []
        prevVal = None
        prevNone = False
        while q:
            cNode = q.pop(0)
            print(cNode)
            if cNode:
                if cNode.left:
                    q.append(cNode.left)
                if cNode.right:
                    q.append(cNode.right)
                prevVal = cNode.val
                prevNone = False
            else:
                if prevNone:
                    break
                prevNone = True
                q.append(None)
                ret.append(prevVal)
        return ret