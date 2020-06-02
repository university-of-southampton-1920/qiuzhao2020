class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.length = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.length < self.maxSize
            self.stack.append(x)
            self.length += 1

    def pop(self) -> int:
        if self.length:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        index = min(k, self.length)
        for i in range(index):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)