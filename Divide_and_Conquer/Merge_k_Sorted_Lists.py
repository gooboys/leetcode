'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
Merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return
        endEarly = None
        for i in lists:
            if not endEarly:
                endEarly = i
        if not endEarly:
            return
        first = 0
        fmin = 10**6
        for i in range(len(lists)):
            if lists[i] and lists[i].val < fmin:
                fmin = lists[i].val
                first = i                
        ret = lists[first]
        prev = lists[first]
        lists[first] = lists[first].next
        index = 1
        while index+1:
            smallest = 10**6
            index = None
            for i in range(len(lists)):
                tempy = lists[i]
                if tempy:
                    if smallest>tempy.val:
                        smallest = tempy.val
                        index = i
            if index == None:
                return ret
            prev.next = lists[index]
            prev = lists[index]
            lists[index] = lists[index].next
    