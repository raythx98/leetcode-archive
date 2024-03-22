# time: O(n)
# space: O(n)
from typing import List
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpn_stack = deque()
        for token in tokens:
            if token in "+-/*":
                r, l = rpn_stack.pop(), rpn_stack.pop()
                if token == '+':
                    rpn_stack.append(l+r)
                elif token == '-':
                    rpn_stack.append(l-r)
                elif token == '/':
                    rpn_stack.append(int(l/r))
                elif token == '*':
                    rpn_stack.append(l*r)
            else:
                rpn_stack.append(int(token))
        return rpn_stack.pop()