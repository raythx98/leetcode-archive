# time: O(n)
# space: O(lgn)
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root):
            if root is None:
                return 0
            left, right = checkHeight(root.left), checkHeight(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return checkHeight(root) != -1