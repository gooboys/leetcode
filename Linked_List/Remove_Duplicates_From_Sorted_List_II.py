'''
82. Remove Duplicates from Sorted List II

Difficulty: Medium
Topics: Linked List, Two Pointers
Companies: Common in technical interviews

Problem Description:
Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

Key Notes:
- The list is guaranteed to be sorted in ascending order.
- Nodes with duplicate values should be removed entirely, leaving only unique numbers.

Examples:

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Explanation:
- Nodes with values 3 and 4 have duplicates, so they are removed.

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
Explanation:
- Nodes with value 1 have duplicates, so they are removed.

Constraints:
1. The number of nodes in the list is in the range [0, 300].
2. -100 <= Node.val <= 100
3. The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        nodes = {}
        dupe = {}
        while head:
            print(head.val)
            if nodes.get(head.val) == None:
                nodes[head.val] = head
                print("Nodupe")
            else:
                dupe[head.val] = 0
                print("dupe")
            head = head.next
            print("")
        keys = nodes.keys()
        keys.sort()
        ret = None
        prev = None
        for i in keys:
            if not prev and dupe.get(i,1):
                ret = nodes[i]
            if prev and dupe.get(i,1):
                prev.next = nodes[i]
            if dupe.get(i,1):
                prev = nodes[i]
        if prev:
            prev.next = None
        return ret