from collections import Counter
class Solution:
    def __init__(self):
        self.t = {}
    
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        self.t = {i:i for i in range(len(graph))}
        for i in range(len(graph)): 
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    self.union(i, j)
        c = Counter()
        for k in self.t:
            c[self.find(k)] += 1
        c1 = Counter()
        for n in initial:
            c1[self.find(n)] += 1
        res = dict()
        ll = c.most_common()
        maxn = ll[0][1]
        flag = maxn
        for p, _ in ll:
            if c[p] == flag:
                res[p] = 1
            if c1[p] == 1:
                res = {}
                break
        flag = -1
        for p, _ in ll:
            if c1[p] == 1:
                flag = c[p]
                break
        for p, _ in ll:
            if c1[p] == 1 and flag == c[p]:
                res[p] = 1
        for n in sorted(initial):
            if self.find(n) in res:
                return n
                
    
    def find(self, x):
        if self.t[x] != x:
            self.t[x] = self.find(self.t[x])
        return self.t[x]
    
    def union(self, x, y):
        self.t[self.find(x)] = self.find(y)
    