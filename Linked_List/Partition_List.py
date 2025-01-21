"""
86. Partition List
Difficulty: Medium

Given the head of a linked list and a value `x`, partition the list such that:
1. All nodes with values less than `x` come before nodes with values greater than or equal to `x`.
2. The original relative order of the nodes in each partition is preserved.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Explanation:
- Nodes less than 3: [1,2,2]
- Nodes greater than or equal to 3: [4,3,5]
- Combined in order: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
Explanation:
- Nodes less than 2: [1]
- Nodes greater than or equal to 2: [2]
- Combined in order: [1,2]

Constraints:
- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head == None:
            return head
        if head.next == None:
            return head
        shead = None
        small = None
        bhead = None
        big = None
        while head:
            if head.val < x:
                if shead == None:
                    shead = head
                    small = head
                else:
                    small.next = head
                    small = head
                head = head.next
            else:
                if bhead == None:
                    bhead = head
                    big = head
                else:
                    big.next = head
                    big = head
                head = head.next
        if small == None:
            return bhead
        elif big == None:
            return shead
        else:
            small.next = bhead
            big.next = None
        return shead