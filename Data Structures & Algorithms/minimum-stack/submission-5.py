class MinStack:

    def __init__(self):
        self.capacity = 4
        self.stack = [0 for i in range(self.capacity)]
        self.min_stack = [0 for i in range(self.capacity)]
        self.pointer = -1

    def push(self, val: int) -> None:
        self.pointer += 1
        if self.pointer == self.capacity:
            self.capacity *= 2
            new_stack = [0] * self.capacity
            new_min_stack = [0] * self.capacity
            new_stack[:self.pointer] = self.stack[:self.pointer]
            new_min_stack[:self.pointer] = self.min_stack[:self.pointer]
            self.stack = new_stack
            self.min_stack = new_min_stack
        self.stack[self.pointer] = val
        if self.pointer == 0:
            self.min_stack[self.pointer] = val
        else:
            self.min_stack[self.pointer] = min(val, self.min_stack[self.pointer - 1])

    def pop(self) -> None:
        pop = self.stack[self.pointer]
        self.pointer -= 1
        return pop

    def top(self) -> int:
        return self.stack[self.pointer]

    def getMin(self) -> int:
        return self.min_stack[self.pointer]