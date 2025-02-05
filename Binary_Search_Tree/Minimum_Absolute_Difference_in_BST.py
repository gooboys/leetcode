'''
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference 
between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Tree Structure:
        4
       / \
      2   6
     / \
    1   3

Explanation: The minimum absolute difference is |2 - 1| = 1 or |3 - 2| = 1.

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Tree Structure:
        1
       / \
      0   48
         /  \
        12   49

Explanation: The minimum absolute difference is |49 - 48| = 1.

Constraints:
- The number of nodes in the tree is in the range [2, 10^4].
- 0 <= Node.val <= 10^5
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        cur = root
        q = []
        ret = 10**5
        prev = - 10**5
        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            ret = min(abs(cur.val - prev), ret)
            prev = cur.val
            cur = cur.right
        return ret        