from collections import Counter
class Solution:  
    def __init__(self):
        self.t = {}
    
    def longestConsecutive(self, nums: List[int]) -> int:
        # init
        if nums == []:
            return 0
        self.t = {i:i for i in nums}
        for n in nums:
            if n-1 in self.t:
                self.union(n, n-1)
            if n+1 in self.t:
                self.union(n, n+1)
        c = Counter()
        for k in self.t:
            c[self.find(k)] += 1
        return c.most_common()[0][1]
            
    def find(self, x):
        # O(1)
        if self.t[x] != x:
            self.t[x] = self.find(self.t[x])
        return self.t[x]
    
    def union(self, x, y):
        self.t[self.find(x)] = self.find(y)