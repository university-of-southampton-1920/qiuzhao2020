class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.size:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        tmp = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += tmp[1]
        return sum(tmp)

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        if k > len(self.stack):
            self.stack[-1][1] += val
        else:
            self.stack[k-1][1] += val
