class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = dict()
        for index, value in enumerate(arr):
            if value in d:
                d[value].append(index)
            else:
                d[value] = [index]
        visited = [False for _ in range(len(arr))]
        waitting = list()
        waitting.append((0,0))
        result = 0
        while len(waitting) != 0:
            index, steps = waitting.pop(0)
            visited[index] = True
            if index == len(arr)-1:
                return steps
            if index+1 < len(arr) and visited[index+1] == False:
                waitting.append((index+1, steps+1))
            if index-1 >= 0 and visited[index-1] == False:
                waitting.append((index-1, steps+1))
            for jump in d[arr[index]]:
                if jump!=index and visited[jump] == False:
                    waitting.append((jump, steps+1))
            d[arr[index]] = []
        return result
