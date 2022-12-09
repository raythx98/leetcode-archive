from collections import deque
class MyQueue:
    def __init__(self):
        self.insert = deque()
        self.to_pop = deque()

    def push(self, x: int) -> None:
        self.insert.append(x)

    def pop(self) -> int:
        if not self.to_pop:
            while self.insert:
                self.to_pop.append(self.insert.pop())
        return self.to_pop.pop()

    def peek(self) -> int:
        if not self.to_pop:
            return self.insert[0]
        return self.to_pop[-1]

    def empty(self) -> bool:
        return not self.insert and not self.to_pop