class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:
        if not self.arr:
            self.arr.append((x, x))
        else:
            self.arr.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()