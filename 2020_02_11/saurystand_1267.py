class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 0 or cols == 0:
            return 0
        
        count = 0
        points = []
        com_per_row = [0] * rows
        com_per_col = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    points.append((i, j))
                    com_per_row[i] += 1 
                    com_per_col[j] += 1
        
        for i, j in points:
            if com_per_row[i] > 1 or com_per_col[j] > 1:
                count += 1
        
        return count





# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         res = 0
#         al = 0
#         row = []
#         col = []
#         for i in range(len(grid)):
#             row.append(sum(grid[i]))
#         for j in range(len(grid[0])):
#             tmp = 0
#             for i in range(len(grid)):
#                 tmp += grid[i][j]
#             col.append(tmp)
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     al += 1
#                     if row[i] == 1 and col[j] == 1:
#                         res += 1
#         return al - res