class MinStack:

    def __init__(self):
        self.stack = []
        self.track_min = -10000

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.track_min = min(val, self.track_min)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_val = self.stack[0]
        for i in self.stack:
            min_val = min(i, min_val)
        return min_val



        
