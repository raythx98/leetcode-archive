# time: O(v) = O(e)
# space: O(v)
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricSubtrees(left, right):
            if not left or not right:
                return left == right
            return left.val == right.val and isSymmetricSubtrees(left.right, right.left) and isSymmetricSubtrees(left.left, right.right)
        return isSymmetricSubtrees(root.left, root.right)