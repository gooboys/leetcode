'''
141. Linked List Cycle

Difficulty: Easy
Topics: Linked List, Two Pointers
Companies: Common in technical interviews

Problem Description:
Given `head`, the head of a linked list, determine if the linked list has a cycle.

Definition:
- A cycle exists in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
- Internally, `pos` is used to denote the index of the node that the tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Task:
Return `True` if there is a cycle in the linked list. Otherwise, return `False`.

Examples:

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: True
Explanation:
- The linked list contains a cycle where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: True
Explanation:
- The linked list contains a cycle where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: False
Explanation:
- The linked list does not contain a cycle.

Constraints:
1. The number of nodes in the list is in the range [0, 10^4].
2. -10^5 <= Node.val <= 10^5
3. `pos` is -1 or a valid index in the linked list.

Follow-Up:
- Can you solve it using O(1) (constant) memory?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tracker = {}
        while head:
            if tracker.get(head,0):
                return True
            tracker[head] = 1
            head = head.next
        return False