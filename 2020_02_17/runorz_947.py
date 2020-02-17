class Solution:
    def find_connected(self,stones,visited, x):
        visited[x] = True
        result = [x]
        for i in range(len(stones)):
            if visited[i] == False:
                if stones[i][0] == stones[x][0] or stones[i][1] == stones[x][1]:
                    result = result + self.find_connected(stones, visited, i)
        return result
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = [False for _ in range(len(stones))]
        groups = list()
        for i in range(len(stones)):
            if visited[i] == False:
                groups.append(self.find_connected(stones,visited,i))
        result = 0
        for e in groups:
            result = result + len(e) - 1
        return result
