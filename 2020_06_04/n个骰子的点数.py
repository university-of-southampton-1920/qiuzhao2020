class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0] * (6*n+1) for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    dp[i][j] += dp[i-1][j-k]
        res = []
        for i in range(n,6*n+1):
            res.append(dp[n][i]/6**n)
        return res


