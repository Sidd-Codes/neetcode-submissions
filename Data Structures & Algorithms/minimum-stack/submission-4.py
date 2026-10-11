class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.min == []:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
