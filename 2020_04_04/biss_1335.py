class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jb = [0] + jobDifficulty
        ml = [[0 for i in range(len(jb))] for j in range(len(jb))]
        for i in range(1, len(jb)):
            ml[i][i] = jb[i]
        for l in range(1, len(jb)):
            for i in range(1, len(jb)-l):
                j = i+l
                ml[i][j] = max(ml[i+1][j], ml[i][j-1])
        dp = [[10**8 for k in range(d+1)] for j in range(len(jb))]
        dp[0][0] = 0
        for i in range(1, len(jb)):
            for k in range(1, d+1):
                if k > i:
                    break
                for j in range(1,i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + ml[j][i])
        return dp[len(jb)-1][d] if dp[len(jb)-1][d] != 10**8 else -1