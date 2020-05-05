class Solution:
    def __init__(self):
        self.dp = None
        self.boxes = None
    
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)
        self.boxes = boxes
        self.dp = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]
        return self.dfs(0, N-1, 0)
    
    def dfs(self, l, r, k):
        if r<l:
            return 0
        if self.dp[l][r][k]:
            return self.dp[l][r][k]
        t = self.dfs(l, r-1, 0) + (k+1) * (k+1)
        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                t = max(t, self.dfs(l, i, k+1) + self.dfs(i+1, r-1, 0))
        self.dp[l][r][k] = t
        return t