"""
61. Rotate List
Difficulty: Medium

Given the head of a linked list, rotate the list to the right by `k` places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Explanation:
- Rotating the list to the right by 2 places results in the list shifting such that the last 2 elements 
  become the first 2 elements.

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
Explanation:
- Since `k = 4` exceeds the length of the list, we take `k % length`, which is 1.
- Rotating the list by 1 place results in the list shifting such that the last element becomes the first.

Constraints:
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10^9
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        if head.next == None:
            return head
        if k == 0:
            return head
        tail = None
        cNode = head
        count = 0
        while cNode:
            count += 1
            if cNode.next == None:
                tail = cNode
            cNode = cNode.next
        tail.next = head
        for i in range(count - k%count - 1):
            head = head.next
        ret = head.next
        head.next = None
        return ret