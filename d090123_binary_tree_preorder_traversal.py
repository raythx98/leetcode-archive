# time: O(n)
# space: O(n)
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class IterativeSolution(object):
    def preorderTraversal(self, root):
        # self, left, right
        if not root:
            return []
        stack = deque([root])
        preorder = []
        while stack:
            nxt = stack.pop()
            preorder.append(nxt.val)
            if nxt.right: stack.append(nxt.right)
            if nxt.left: stack.append(nxt.left)
        return preorder
class RecursiveSolution(object):
    def preorderTraversal(self, root):
        # self, left, right
        def getPreorderTravel(root, order):
            if not root:
                return order
            order.append(root.val)
            getPreorderTravel(root.left, order)
            getPreorderTravel(root.right, order)
            return order
        return getPreorderTravel(root, [])