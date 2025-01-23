'''
117. Populating Next Right Pointers in Each Node II

Difficulty: Medium
Topics: Tree, Breadth-First Search (BFS), Binary Tree
Companies: Common in technical interviews

Problem Description:
Given a binary tree, populate each `next` pointer in the tree nodes to point to its next right node. 
If there is no next right node, the `next` pointer should be set to NULL.

Tree Node Structure:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Key Details:
1. Initially, all `next` pointers are set to NULL.
2. The tree is not necessarily a perfect binary tree (some nodes may be missing children).

Examples:

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation:
- Given the binary tree:
        1
      /   \
     2     3
    / \      \
   4   5      7
- Your function should populate each `next` pointer so the tree becomes:
        1 -> NULL
      /   \
     2  -> 3 -> NULL
    / \      \
   4-> 5 ->   7 -> NULL
- The serialized output represents this level-order traversal with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
Explanation:
- An empty tree should remain empty.

Constraints:
1. The number of nodes in the tree is in the range [0, 6000].
2. -100 <= Node.val <= 100
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q = [root,None]
        prev = None
        prevNone = False
        while q:
            cNode = q.pop(0)
            if cNode:
                if prev:
                    prev.next = cNode
                if cNode.left:
                    q.append(cNode.left)
                if cNode.right:
                    q.append(cNode.right)
                prev = cNode
                prevNone = False
            elif prevNone:
                break
            else:
                prevNone = True
                q.append(None)
                prev = None
        return root