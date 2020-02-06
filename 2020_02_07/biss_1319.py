class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        if len(connections) < n-1:
            return -1
        for con in connections:
            graph[con[0]].add(con[1])
            graph[con[1]].add(con[0])
        mark = [0 for i in range(n)]
        res = 0
        for i in range(n):
            if mark[i] != 1:
                res += 1
            self.dfs(graph, mark, i)
        return res -1
        
    def dfs(self, graph, mark, node):
        if mark[node] == 1:
            return
        mark[node] = 1
        for next_node in graph[node]:
            self.dfs(graph, mark, next_node)