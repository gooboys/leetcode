'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where:
- preorder is the preorder traversal of a binary tree.
- inorder is the inorder traversal of the same tree.

Construct and return the binary tree.

Example 1:
Input: 
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Constructed Tree:
        3
       / \
      9   20
         /  \
        15   7

Explanation:
- Preorder (Root -> Left -> Right): [3,9,20,15,7]
- Inorder  (Left -> Root -> Right): [9,3,15,20,7]
- Using these traversals, we can reconstruct the tree as shown above.

Example 2:
Input: 
preorder = [-1]
inorder  = [-1]
Output: [-1]

Constructed Tree:
       -1

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 0:
            return None
        index = inorder.index(preorder[0])
        leftLen = len(inorder[:index])
        rLen = len(inorder[index+1:])
        ret = TreeNode(preorder[0])
        ret.left = self.buildTree(preorder[1:leftLen+1],inorder[:index])
        ret.right = self.buildTree(preorder[leftLen+1:],inorder[index+1:])
        return ret