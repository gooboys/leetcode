'''
133. Clone Graph

Difficulty: Medium
Topics: Graph, Depth-First Search, Breadth-First Search
Companies: Common in technical interviews

Problem Description:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Graph Definition:
1. Each node in the graph contains:
   - A value (`val`) which is an integer.
   - A list (`neighbors`) of other nodes that are its neighbors.
   - Example:
     class Node {
         public int val;
         public List<Node> neighbors;
     }

Test Case Format:
- Each node's value corresponds to its index (1-indexed).
- The graph is represented using an adjacency list, where:
  - Each list describes the set of neighbors of a node in the graph.
  - The graph starts with the node of `val = 1`.

Task:
- Return the deep copy of the graph. A deep copy means that no pointers in the new graph should refer to nodes in the original graph.

Examples:

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation:
- The graph contains 4 nodes:
  - Node 1's neighbors: 2, 4
  - Node 2's neighbors: 1, 3
  - Node 3's neighbors: 2, 4
  - Node 4's neighbors: 1, 3

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation:
- The graph contains only one node (val = 1), and it has no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation:
- The graph is empty and contains no nodes.

Constraints:
1. The number of nodes in the graph is in the range [0, 100].
2. 1 <= Node.val <= 100
3. `Node.val` is unique for each node.
4. There are no repeated edges or self-loops in the graph.
5. The graph is connected, and all nodes can be visited starting from the given node.
'''



# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        if not node.neighbors:
            return Node(node.val)
        q = [node]
        visited = {}
        neighbors = {}
        ids = {}
        while q:
            cNode = q.pop(0)
            visited[cNode.val] = 0
            tempneighs = []
            for i in cNode.neighbors:
                tempneighs.append(i.val)
                if visited.get(i.val,1):
                    q.append(i)
                    visited[i.val] = 0
            neighbors[cNode.val] = tempneighs
            newNode = Node(cNode.val)
            ids[cNode.val] = newNode
        allNodes = ids.keys()
        for part in allNodes:
            cNode = ids[part]
            tempNeigh = []
            for neigh in neighbors[part]:
                tempNeigh.append(ids[neigh])
            cNode.neighbors = tempNeigh
        return ids[allNodes[0]]