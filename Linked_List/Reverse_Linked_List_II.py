'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Linked List Before Reversal:
1 -> 2 -> 3 -> 4 -> 5

Reversing nodes from position 2 to 4:
1 -> (4 -> 3 -> 2) -> 5

Linked List After Reversal:
1 -> 4 -> 3 -> 2 -> 5

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Linked List Before and After Reversal:
5  (No change as left == right)

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        track = {}
        count = 1
        cNode = head
        while cNode:
            track[count] = cNode
            count += 1
            cNode = cNode.next
        for i in range(right-left):
            temp = track[right-i]
            temp.next = track[right-i-1]
        track[left].next = track.get(right+1, None)
        if left != 1:
            track[left-1].next = track[right]
            return head
        else:
            return track[right]
        