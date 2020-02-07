class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        l = [i for i in range(n)]
        def root(i):
            while l[i] != i:
                l[i] = l[l[i]]
                i = l[i]
            return i
        for i, j in connections:
            i = root(i)
            j = root(j)
            if i != j:
                n -= 1
                l[i] = j
        return n - 1
            