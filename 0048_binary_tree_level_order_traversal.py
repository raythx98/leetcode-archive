# time: O(v) = O(e)
# space: O(v)
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curr_level, ans = [root], []
        while curr_level:
            ans += [[node.val for node in curr_level]]
            nodes = [(node.left, node.right) for node in curr_level]
            curr_level = [node for LR in nodes for node in LR if node]
        return ans