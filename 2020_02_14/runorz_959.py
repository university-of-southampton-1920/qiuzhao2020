class Solution:
    def coloring(self,edge, x, y):
        edge[x][y] = -1
        length = len(edge)
        if x+1 < length:
            if edge[x+1][y] == 0:
                self.coloring(edge, x+1, y)
        if x-1 >= 0:
            if edge[x-1][y] == 0:
                self.coloring(edge, x-1, y)
        if y+1 < length:
            if edge[x][y+1] == 0:
                self.coloring(edge, x, y+1)
        if y-1 >= 0:
            if edge[x][y-1] == 0:
                self.coloring(edge, x, y-1)
        return
    
    def regionsBySlashes(self, grid: List[str]) -> int:
        l = len(grid)
        m = [[0 for _ in range(3*l)] for _ in range(3*l)]
        for rindex, row in enumerate(grid):
            for cindex, column in enumerate(row):
                if column == '/':
                    m[3*rindex][3*cindex+2] = 1
                    m[3*rindex+1][3*cindex+1] = 1
                    m[3*rindex+2][3*cindex] = 1

                if column == '\\':
                    m[3*rindex][3*cindex] = 1
                    m[3*rindex+1][3*cindex+1] = 1
                    m[3*rindex+2][3*cindex+2] = 1
                if column == ' ':
                    continue
        result = 0
        for rindex, row in enumerate(m):
            for cindex, column in enumerate(row):
                if column == 0:
                    self.coloring(m, rindex, cindex)
                    result = result + 1
        return result
