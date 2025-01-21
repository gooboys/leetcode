"""
25. Reverse Nodes in k-Group
Difficulty: Hard

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

Rules:
1. `k` is a positive integer and is less than or equal to the length of the linked list.
2. If the number of nodes is not a multiple of `k`, the remaining nodes at the end should remain in their original order.
3. The values of the nodes cannot be altered; only the nodes themselves may be rearranged.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is `n`.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        stack = []
        cNode = head
        for i in range(k):
            stack.insert(0,cNode)
            cNode = cNode.next
        cNode = stack[0].next
        ret = stack[0]
        prev = ret
        for i in stack:
            prev.next = i
            prev = i
        prev.next = cNode
        last = prev
        while cNode:
            stack = []
            for i in range(k):
                if cNode == None:
                    return ret
                stack.insert(0,cNode)
                cNode = cNode.next
            cNode = stack[0].next
            for i in stack:
                prev.next = i
                prev = i
            prev.next = cNode
            last = prev
            if cNode == None:
                return ret
        return ret
