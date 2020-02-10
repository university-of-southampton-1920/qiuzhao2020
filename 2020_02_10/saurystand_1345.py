class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # bfs
        # it can also use deque
        if len(set(arr)) == len(arr):
            return len(arr)-1
        conn = collections.defaultdict(set)
        for i,val in enumerate(arr):
            conn[val].add(i)
        res,cur,seen,visit = 0, {0}, {0},set()
        while len(arr)-1 not in seen:
            res += 1
            tmp = set()
            for node in seen:
                if node -1 > 0 and node-1 not in seen: tmp.add(node-1)
                if arr[node] not in visit:
                    tmp |= (conn[arr[node]] - seen)
                    visit.add(arr[node])
                if node +1 < len(arr) and node + 1 not in seen: tmp.add(node + 1)
            tmp -= seen
            seen |= tmp
            cur = tmp
        return res