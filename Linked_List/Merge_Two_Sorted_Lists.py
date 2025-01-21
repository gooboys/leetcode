"""
21. Merge Two Sorted Lists
Difficulty: Easy

You are given the heads of two sorted linked lists, list1 and list2. The task is to merge the two lists into one sorted linked list. 
The merged list should be created by splicing together the nodes of the two input lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = list1
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list2.val<list1.val:
            ret = list2
            list2 = list2.next
        else:
            list1 = list1.next
        prev = ret
        while list1 != None or list2 != None:
            if list1 == None:
                prev.next = list2
                prev = list2
                list2 = list2.next
            elif list2 == None:
                prev.next = list1
                prev = list1
                list1 = list1.next
            elif list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        return ret