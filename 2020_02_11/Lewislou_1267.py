class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        list1 = []
        server = []
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[1])):
                if(grid[i][j]) == 1:
                    list1.append([i,j])
        for [i,j] in list1:
            if(len([[a,b] for [a,b] in list1 if a == i]) > 1):
                server.extend([[a,b] for [a,b] in list1 if a == i])
            if(len([[a,b] for [a,b] in list1 if b == j]) > 1):
                server.extend([[a,b] for [a,b] in list1 if b == j])
        server = list(set([tuple(t) for t in server]))
        return(len(server))