class StockSpanner:

    def __init__(self):
        self.stack = [(0, 10**8)]
        self.c = 0

    def next(self, price: int) -> int:
        self.c += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        t = self.c - self.stack[-1][0]
        self.stack.append((self.c, price))
        return t