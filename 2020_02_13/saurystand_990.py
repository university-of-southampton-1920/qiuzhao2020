class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = self.getParent(equations)
        for e in equations:
            if e[1] == "=":
                self.union(parents, e[0], e[3])###
        for e in equations:
            if e[1] == "!":
                leftRoot = self.find(parents, e[0])
                rightRoot = self.find(parents, e[3])
                if leftRoot == rightRoot:
                    return False
        return True
    
    def find(self, parents, node):
        if parents[node] != node:
            parents[node] = self.find(parents, parents[node])
        return parents[node]
        
    def union(self, parents, x, y):
        rootA = self.find(parents, x)
        rootB = self.find(parents, y)
        if rootA != rootB:
            parents[rootB] = rootA
    
    
    
    def getParent(self, equations):
        parents = collections.defaultdict()
        for e in equations:
            parents[e[0]] = e[0]
            parents[e[3]] = e[3]
        return parents
             




# from collections import defaultdict, Counter
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         table = dict()
#         for a, _, _, b in equations:
#             table[a] = a
#             table[b] = b
#         for e in equations:
#             if e[1] == "=":
#                 table[self.find(table, e[0])] = self.find(table, e[3])
#         for e in equations:
#             if e[1] == "!":
#                 if self.find(table, e[0]) == self.find(table, e[3]):
#                     return False
#         return True
    
#     def find(self, table, x):
#         if x != table[x]:
#             table[x] = self.find(table, table[x])
#         return table[x]