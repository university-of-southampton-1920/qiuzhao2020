import numpy as np
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = []
        np_grid = np.array(grid)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if np_grid[i,j] == 1:
                    if 1 in (np_grid[i,:j].tolist() + np_grid[i,j+1:].tolist()):
                        result = result + 1
                    elif 1 in (np_grid[:i,j].tolist() + np_grid[i+1:,j].tolist()):
                        result = result + 1
        return result
