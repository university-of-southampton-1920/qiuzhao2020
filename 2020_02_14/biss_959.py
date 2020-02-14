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