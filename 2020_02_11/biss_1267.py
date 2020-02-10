class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        al = 0
        row = []
        col = []
        for i in range(len(grid)):
            row.append(sum(grid[i]))
        for j in range(len(grid[0])):
            tmp = 0
            for i in range(len(grid)):
                tmp += grid[i][j]
            col.append(tmp)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    al += 1
                    if row[i] == 1 and col[j] == 1:
                        res += 1
        return al - res