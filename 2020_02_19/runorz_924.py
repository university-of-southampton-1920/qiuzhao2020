class Solution:
    def find_connected(self,graph, visited, x):
        visited[x] = True
        temp_group = [x]
        for y in range(len(graph)):
            if graph[x][y] == 1 and x != y and visited[y]==False:
                temp_group = temp_group + self.find_connected(graph, visited, y)
        return temp_group
    
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        visited = [False for _ in range(len(graph))]
        groups = list()
        initial = sorted(initial)
        for i in range(len(graph)):
            if visited[i] == False:
                visited[i] = True
                temp_group = [i]
                for j in range(len(graph)):
                    if graph[i][j] == 1 and i!=j and visited[j] == False:
                        temp_group = temp_group + self.find_connected(graph, visited, j)
                groups.append(temp_group)

        malware = [[] for _ in range(len(groups))]

        for e in initial:
            for i in range(len(groups)):
                if e in groups[i]:
                    malware[i].append(e)
                    break

        max_num = 0

        for i in range(len(groups)):
            if len(malware[i]) != 0 and len(groups[i]) > max_num:
                result = malware[i][0]
                max_num = len(groups[i])

        return result
