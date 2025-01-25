'''
637. Average of Levels in Binary Tree

Difficulty: Easy
Topics: Tree, Breadth-First Search, Queue
Companies: Common in technical interviews

Problem Description:
Given the `root` of a binary tree, return the average value of the nodes at each level in the form of an array. 
Answers within 10^-5 of the actual answer will be accepted.

Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation:
- Level 0: The average value is 3.
- Level 1: The average value is (9 + 20) / 2 = 14.5.
- Level 2: The average value is (15 + 7) / 2 = 11.
- Hence, return [3.00000, 14.50000, 11.00000].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation:
- Level 0: The average value is 3.
- Level 1: The average value is (9 + 20) / 2 = 14.5.
- Level 2: The average value is (15 + 7) / 2 = 11.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. -2^31 <= Node.val <= 2^31 - 1
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []
        q = [root]
        ret = []
        while q:
            tempSum = 0.000
            tempLen = len(q)
            for _ in range(tempLen):
                cNode = q.pop(0)
                if cNode.left:
                    q.append(cNode.left)
                if cNode.right:
                    q.append(cNode.right)
                tempSum += float(cNode.val)
            ret.append(tempSum/float(tempLen))
        return ret