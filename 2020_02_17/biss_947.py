from collections import defaultdict
class Solution:
    def __init__(self):
        self.t = {}
    
    def removeStones(self, stones: List[List[int]]) -> int:
        self.t = {i:i for i in range(len(stones))}
        row = defaultdict(list)
        col = defaultdict(list)
        for i, s in enumerate(stones):
            row[s[0]].append(i)
            col[s[1]].append(i)
            if row[s[0]][0] != i:
                self.union(i, row[s[0]][0])
            if col[s[1]][0] != i:
                self.union(i, col[s[1]][0])
        return len(stones) - len(set(self.find(x) for x in self.t))
    
    def find(self, x):
        if self.t[x] != x:
            self.t[x] = self.find(self.t[x])
        return self.t[x]
    
    def union(self, x, y):
        self.t[self.find(x)] = self.find(y)