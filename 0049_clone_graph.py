# time: O(v + e)
# space: O(v)
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        created = {node: Node(node.val)}
        frontier = deque([node])
        while frontier:
            curr_node = frontier.popleft()
            for nb in curr_node.neighbors:
                # create neighbors if not already created
                if nb not in created:
                    created[nb] = Node(nb.val)
                    frontier.append(nb)
                
            # connect new neighbour
            created[curr_node].neighbors = [created[nb] for nb in curr_node.neighbors]
        return created[node]
        