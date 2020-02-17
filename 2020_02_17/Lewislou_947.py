class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_repres = {}
        col_repres = {}
        graph = {}
        for x, y in stones:
            if x not in row_repres:
                row_repres[x] = (x,y)
            if y not in col_repres:
                col_repres[y] = (x,y)
            graph[(x,y)] = []
            if row_repres[x] != (x,y):
                graph[row_repres[x]].append((x,y))
                graph[(x,y)].append(row_repres[x])
            if col_repres[y] != (x,y):
                graph[col_repres[y]].append((x,y))
                graph[(x,y)].append(col_repres[y])
        
        def dfs(x,y,visited):
            visited.add((x,y))
            for nb_x, nb_y in graph[(x,y)]:
                if (nb_x, nb_y) not in visited:
                    dfs(nb_x, nb_y,visited)
        
        num_islands = 0
        visited = set()
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x,y,visited)
                num_islands += 1
        
        return len(stones) - num_islands