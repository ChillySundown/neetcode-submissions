class MinStack:

    def __init__(self):
        self.num_stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        if(not self.min_stack or val <= self.min_stack[-1]):
            self.min_stack.append(val)
        self.num_stack.append(val)

    def pop(self) -> None:
        if(self.num_stack[-1] == self.min_stack[-1]):
            self.min_stack.pop()
        self.num_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
