class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ids = {}
        size = {}
        def find(p):
            if p not in ids:
                ids[p] = p
                return p
            while not p == ids[p]:
                ids[p] = ids[ids[p]]
                p = ids[p]
            return p
        def union(p,q, count):
            rp = find(p)
            rq = find(q)
            if not rp == rq:
                sp = size.get(rp,1)
                sq = size.get(rq,1)
                count += 1
                if sp < sq:
                    ids[rp] = ids[rq]
                    size[rq] = sp + sq
                else:
                    ids[rq] = ids[rp]
                    size[rp] = sp + sq
            return count
        
        c = {}
        M = len(row) // 2
        count = 0
        for i in range(M):
            c[row[2*i]] = c[row[2*i+1]] = i
        for i in range(M):
            count = union(c[2*i],c[2*i+1], count)
            
        return count
    
    
    
# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         obj = unionFind()
#         length = len(row)
#         for i in range(length):
#             row[i] = row[i] / 2
            
#         for i in range(length):
#             obj.union(row[i], row[i+1])
#             i += 2
#         return row.length - obj.components()

# class unionFind:
#     def __init__(self):
#         self.arr = []
#         self.rank = []
#     def unionFind(self, size):
#         self.arr = [0] * size
#         for i in range(size):
#             self.arr[i] = i
#         self.rank = [0] * size
#     def union(self, a, b):
#         parent1 = self.find(a)
#         parent2 = self.find(b)
#         if parent1 == parent2:
#             return False
#         if self.rank[parent2] > self.rank[parent1]:
#             self.arr[parent1] = parent2 # change 
#             self.rank[parent2] += 1
#         return True
#     def find(self, a:int):
#         if self.arr[a] == a:
#             return a
#         arr[a] = self.find(arr[a])
#         return self.arr[a]
#     def components():
#         count = 0
#         length = len(self.arr)
#         for i in range(length):
#             if i == self.arr[i]:
#                 count += 1
#         return count
        
    
    
    
    
    
    