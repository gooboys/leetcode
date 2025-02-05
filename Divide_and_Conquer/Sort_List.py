'''
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Linked List Before Sorting:
4 -> 2 -> 1 -> 3

Linked List After Sorting:
1 -> 2 -> 3 -> 4

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Linked List Before Sorting:
-1 -> 5 -> 3 -> 4 -> 0

Linked List After Sorting:
-1 -> 0 -> 3 -> 4 -> 5

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        tracker = {}
        while head:
            tracker[head.val] = tracker.get(head.val,[])
            tracker[head.val].append(head)
            head = head.next
        vals = list(tracker.keys())
        vals.sort()
        prev = tracker[vals[0]][0]
        for i in vals:
            current = tracker[i]
            if prev and len(current) == 1:
                prev.next = current[0]
                prev = current[0]
            elif prev:
                for j in current:
                    prev.next = j
                    prev = j
        tracker[vals[-1]][-1].next = None
        return tracker[vals[0]][0]