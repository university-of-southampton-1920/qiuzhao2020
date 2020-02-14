class Solution:
    def __init__(self):
        self.table = {}
    
    def find(self, x):
        if self.table[x] != x:
            self.table[x] = self.find(self.table[x])
        return self.table[x]
    
    def union(self, x, y):
        self.table[self.find(x)] = self.find(y)
    
    def minSwapsCouples(self, row: List[int]) -> int:
        self.table = {i:i for i in range(int(len(row)/2) )}
        res = 0
        for i in range(0, len(row), 2):
            g1 = int(row[i] / 2)
            g2 = int( (row[i+1])/2)
            if g1 != g2:
                if self.find(g1) != self.find(g2):
                    self.union(g1, g2)
                    res += 1
        return res