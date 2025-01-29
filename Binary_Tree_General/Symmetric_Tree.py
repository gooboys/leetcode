'''
101. Symmetric Tree

Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Examples:

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: True
Explanation:
    1
   / \
  2   2
 / \ / \
3  4 4  3
- The tree is symmetric because the left and right subtrees are mirrors of each other.

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: False
Explanation:
    1
   / \
  2   2
   \    \
   3     3
- The tree is not symmetric because the left and right subtrees are not mirrors of each other.

Constraints:
1. The number of nodes in the tree is in the range [1, 1000].
2. -100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        rq = [root]
        lq = [root]
        while rq and lq:
            cright = rq.pop(0)
            cleft = lq.pop(0)
            if cright and cleft:
                if cright.val != cleft.val:
                    return False
            else:
                if cright != cleft:
                    return False
            if cright:
                if cright.right:
                    rq.append(cright.right)
                else:
                    rq.append(0)
                if cright.left:
                    rq.append(cright.left)
                else:
                    rq.append(0)
            if cleft:
                if cleft.left:
                    lq.append(cleft.left)
                else:
                    lq.append(0)
                if cleft.right:
                    lq.append(cleft.right)
                else:
                    lq.append(0)
        return True