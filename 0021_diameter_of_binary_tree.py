# time: O(v) = O(e)
# space: O(v)
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverseHeight(root, max_diameter):
            if not root:
                return -1
            left, right = traverseHeight(root.left, max_diameter), traverseHeight(root.right, max_diameter)
            if left + right + 2 > max_diameter[0]:
                max_diameter[0] = left + right + 2
            return 1 + max(left, right)
        max_diameter = [0]
        traverseHeight(root, max_diameter)
        return max_diameter[0]