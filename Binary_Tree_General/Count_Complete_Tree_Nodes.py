'''
222. Count Complete Tree Nodes

Difficulty: Easy
Topics: Tree, Binary Search
Companies: Common in technical interviews

Problem Description:
Given the `root` of a complete binary tree, return the number of nodes in the tree.

Definition:
- A complete binary tree is defined as a binary tree where every level, except possibly the last, is completely filled, 
  and all nodes in the last level are as far left as possible.
- The number of nodes in the last level is between 1 and 2^h (inclusive), where `h` is the height of the tree.

Task:
Design an algorithm that runs in less than O(n) time complexity.

Examples:

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6
Explanation:
    1
   / \
  2   3
 / \  /
4  5 6
- The tree contains 6 nodes.

Example 2:
Input: root = []
Output: 0
Explanation:
- The tree is empty, so there are no nodes.

Example 3:
Input: root = [1]
Output: 1
Explanation:
- The tree contains only one node.

Constraints:
1. The number of nodes in the tree is in the range [0, 5 * 10^4].
2. 0 <= Node.val <= 5 * 10^4
3. The tree is guaranteed to be complete.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        ret = 0
        while q:
            ret += 1
            cNode = q.pop(0)
            if cNode.right:
                q.append(cNode.right)
            if cNode.left:
                q.append(cNode.left)
        return ret