class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #draw a draft would have a clue
        stones = list(map(tuple, stones))
        s = set(stones)
        d = collections.defaultdict(list)
        for i, j in s:
            d[i].append(j)
            d[j].append(i)
        
        def dfs(i,j): #stand for x and y axis
            for x in d[j]: #find all points when y=j
                if (x,j) not in s:
                    continue
                s.remove((x,j))
                dfs(x,j)
            for y in d[i]: #find all points when x=i
                if (i,y) not in s:
                    continue
                s.remove((i,y))
                dfs(i,y)
        
        slength = len(s)
        result = 0
        for x,y in stones:
            if (x,y) not in s: 
                continue
            s.remove((x,y))
            dfs(x,y)
            #n-len(s) represent the length of graph, e.g. the number of element removed through dfs
            result += slength - len(s) - 1
            slength = len(s)
        
        return result
            
            