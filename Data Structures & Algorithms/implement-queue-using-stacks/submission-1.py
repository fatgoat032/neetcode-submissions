class MyQueue:

    def __init__(self):
        self.pointer = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.pointer += 1
        return self.stack[self.pointer - 1]

    def peek(self) -> int:
        return self.stack[self.pointer]

    def empty(self) -> bool:
        if not self.stack[self.pointer:]:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()