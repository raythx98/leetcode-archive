# time: O(v+e)
# space: O(v+e)
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list) # directed tree
        subtree_nodes = [1 for i in range(n)]
        for ai, bi in edges:
            adj_list[ai].append(bi)
            adj_list[bi].append(ai)

        def count_nodes(root):
            if not adj_list[root]:
                subtree_nodes[root] = 1
                return 1
            size = 1
            for i in adj_list[root]:
                # in each subtree, remove bi-directional edge
                # to prevent infinite loop
                adj_list[i].remove(root)
                # increase size
                size += count_nodes(i)

            subtree_nodes[root] = size
            return size

        answer = [0 for i in range(n)]
        def get_distances(root, distance):
            answer[root] = distance
            for i in adj_list[root]:
                # i will become new root
                get_distances(i, distance - subtree_nodes[i] + (n - subtree_nodes[i]))
            
        total_distance = -count_nodes(0) + sum(subtree_nodes)
        get_distances(0, total_distance)
        return answer
        
