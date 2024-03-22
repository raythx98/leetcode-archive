# time: O(lgn)
# space: O(lgn)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minNode, maxNode, currNode = min(p.val, q.val), max(p.val, q.val), root.val
        if minNode <= currNode and maxNode >= currNode:
            return root
        elif minNode > currNode:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
        