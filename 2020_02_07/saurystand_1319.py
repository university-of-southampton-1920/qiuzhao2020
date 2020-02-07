class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        sorted(connections)
        
        if len(connections) < n - 1:
            return -1
        
        data = [[] for _ in range(n)]
        
        for c in connections:
            data[c[0]].append(c[1])
            data[c[1]].append(c[0])
            
        visited = [0] * n
        
        result = 0
        for i in range(n):
            if visited[i] == 0:
                result += 1
                self.dfs(data, visited, i)
        return result - 1
    
    def dfs(self, data, visited, idx):
        visited[idx] = 1 #visited
        for v in data[idx]:
            if visited[v] == 0:
                self.dfs(data, visited, v)
        