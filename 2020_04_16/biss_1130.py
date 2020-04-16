class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[[0, 1] for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i][1] = arr[i]
        for l in range(1, len(arr)):
            for i in range(len(arr)-l):
                j = i + l
                dp[i][j][0] = 10**8
                for m in range(i, j):
                    dp[i][j][0] = min( dp[i][j][0], dp[i][m][0] + dp[m+1][j][0] + dp[i][m][1] * dp[m+1][j][1] )
                    dp[i][j][1] = max( dp[i][j][1], dp[i][m][1], dp[m+1][j][1])
        
        return dp[0][len(arr)-1][0]