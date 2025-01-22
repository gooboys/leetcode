'''
129. Sum Root to Leaf Numbers

Difficulty: Medium
Topics: Tree, Depth-First Search
Companies: Common in technical interviews

Problem Description:
You are given the root of a binary tree containing digits from 0 to 9 only. 
Each root-to-leaf path in the tree represents a number.

Definition:
- A root-to-leaf path like 1 -> 2 -> 3 represents the number 123.
- Return the total sum of all root-to-leaf numbers.

Key Notes:
- A leaf node is a node with no children.
- Test cases are generated such that the answer will fit in a 32-bit integer.

Examples:

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
- The root-to-leaf path 1->2 represents the number 12.
- The root-to-leaf path 1->3 represents the number 13.
- Sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
- The root-to-leaf path 4->9->5 represents the number 495.
- The root-to-leaf path 4->9->1 represents the number 491.
- The root-to-leaf path 4->0 represents the number 40.
- Sum = 495 + 491 + 40 = 1026.

Constraints:
1. The number of nodes in the tree is in the range [1, 1000].
2. 0 <= Node.val <= 9
3. The depth of the tree will not exceed 10.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = [root]
        prev = {}
        leaves = []
        while q:
            node = q.pop(0)
            if not (node.left or node.right):
                leaves.append(node)
            if node.left:
                prev[node.left] = node
                q.append(node.left)
            if node.right:
                prev[node.right] = node
                q.append(node.right)
        total = 0
        for i in leaves:
            cNode = i
            string = []
            while cNode != root:
                string.append(cNode.val)
                cNode = prev[cNode]
            string.append(cNode.val)
            tens = len(string)
            for i in range(tens):
                total += string[i]*(10**i)
        return total