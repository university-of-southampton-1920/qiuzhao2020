class Solution:
    #dont know how to do
    def __init__(self):
        self.N = 0
        self.parents = []
        self.ranks = []
        
    def regionsBySlashes(self, grid: List[str]) -> int:        
        def Find(x: int):
            while x != self.parents[x]:
                self.parents[x] = self.parents[self.parents[x]]
                x = self.parents[x]
            return x
        
        def Union(x: int, y: int):
            rootx, rooty = Find(x), Find(y)
            if rootx == rooty:
                return False
            if self.ranks[rootx] > self.ranks[rooty]:
                self.parents[rooty] = rootx
            elif self.ranks[rooty] > self.ranks[rootx]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                self.ranks[rootx] += 1
            return True
        
        def loc(i: int, j: int):
            return self.N*i+j
   
        res = 0
        self.N = len(grid) + 1
        self.parents = [i for i in range(self.N **2)]
        self.ranks = [0] * (self.N **2)
        edges = []
        for i in range(self.N-1):
            for j in range(self.N-1):
                if grid[i][j] == '/':
                    edges.append([loc(i, j+1), loc(i+1, j)])                  
                if grid[i][j] == '\\':
                    edges.append([loc(i,j), loc(i+1,j+1)])
                if i == 0:
                    edges.append([loc(i,j), loc(i, j+1)])
                if i == self.N - 2:
                    edges.append([loc(i+1,j), loc(i+1,j+1)])
                if j == 0:
                    edges.append([loc(i,j), loc(i+1,j)])
                if j == self.N - 2:
                    edges.append([loc(i,j+1), loc(i+1,j+1)])
        for edge in edges:
            res += 1 if not Union(edge[0], edge[1]) else 0
        return res




class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        table = {}
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i > 0:
                    self.union(table, (i-1, j, 2), (i, j, 0))
                if j > 0:
                    self.union(table, (i, j-1, 1), (i, j, 3))
                if grid[i][j] == "\\":
                    self.union(table, (i, j, 0), (i, j, 1))
                    self.union(table, (i, j, 3), (i, j, 2))
                elif grid[i][j] == "/":
                    self.union(table, (i, j, 0), (i, j, 3))
                    self.union(table, (i, j, 1), (i, j, 2))
                else:
                    self.union(table, (i, j, 0), (i, j, 1))
                    self.union(table, (i, j, 1), (i, j, 2))
                    self.union(table, (i, j, 2), (i, j, 3))
        print(table)
        return len(set(self.find(table, k) for k in table))
                    
                    
    def union(self,table, x, y):
        table[self.find(table, x)] = self.find(table, y)
    
    def find(self, table, x):
        if not (x in table):
            table[x] = x
        if table[x] != x:
            table[x] = self.find(table, table[x])
        return table[x]