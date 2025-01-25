'''
138. Copy List with Random Pointer

Difficulty: Medium
Topics: Linked List, Hash Table
Companies: Common in technical interviews

Problem Description:
A linked list of length `n` is given where each node contains:
1. A `val` attribute (an integer).
2. A `random` pointer that could point to any node in the list, or `null`.

Task:
Construct a **deep copy** of the linked list. The deep copy should:
1. Consist of exactly `n` brand new nodes.
2. Maintain the same `val`, `next`, and `random` pointer structure as the original list.
3. Ensure none of the pointers in the new list point to nodes in the original list.

Key Notes:
- If there are two nodes `X` and `Y` in the original list where `X.random --> Y`, 
  then in the copied list, `x.random --> y` (the deep copy of `X` and `Y`).

Input/Output Representation:
- The linked list is represented as a list of `n` nodes. 
- Each node is represented as a pair `[val, random_index]` where:
  - `val`: Integer representing the node value.
  - `random_index`: The index of the node (range from 0 to n-1) that the `random` pointer points to, 
    or `null` if it does not point to any node.

Examples:

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
1. 0 <= n <= 1000
2. -10^4 <= Node.val <= 10^4
3. `Node.random` is either `null` or points to a valid node in the list.
'''

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        newHead = Node(head.val)
        rando = {head:head.random}
        new = {head:newHead}
        cNode = head
        pNode = None
        while cNode:
            newNode = Node(cNode.val)
            if pNode:
                pNode.next = newNode
            rando[cNode] = cNode.random
            new[cNode] = newNode
            pNode = newNode
            cNode = cNode.next
        for i in new.keys():
            temp = new[i]
            randoKey = rando[i]
            trueRand = new.get(randoKey, None)
            temp.random = trueRand
        return new[head]
