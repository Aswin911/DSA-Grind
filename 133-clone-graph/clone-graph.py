"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]

            clone_node = Node(node.val)
            oldToNew[node] = clone_node

            for nei in node.neighbors:
                clone_node.neighbors.append(clone(nei))
            
            return clone_node
        
        return clone(node) if node else None