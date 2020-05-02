
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for k in range(16)] for j in range(6)] for i in range(n+1)]
        M = 10**9 + 7
        for i in range(6):
            dp[1][i][1] = 1
        for i in range(1, n+1):
            for j in range(6):
                for k in range(1, rollMax[j]+1):
                    if k > 1:
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else:
                        for jj in range(6):
                            if jj == j:
                                continue
                            for kk in range(1, rollMax[jj]+1):
                                dp[i][j][k] += dp[i-1][jj][kk]
                    # print("i",i, "j", j, "k",k, "v",dp[i][j][k])
        res = 0
        for jj in range(6):
            for kk in range(1, rollMax[jj]+1):
                res += dp[n][jj][kk]
        return res % M