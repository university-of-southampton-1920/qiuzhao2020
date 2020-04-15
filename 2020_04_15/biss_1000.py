class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        L = len(stones)
        INT_MAX = 10**8
        dp = [[[INT_MAX for k in range(K+1)] for i in range(L)] for j in range(L)]
        if L == 1:
            return 0
        if (L-1) % (K-1) != 0:
            return -1
        presum = [0 for i in range(L)]
        presum[0] = stones[0]
        for i in range(1, L):
            presum[i]=presum[i-1]+stones[i]
        for i in range(L):
            dp[i][i][1] = 0
        for l in range(1, L):
            for i in range(L-l):
                j = i+l
                for k in range(2,K+1):
                    for m in range(i,j):
                        if dp[i][m][1] == INT_MAX or dp[m+1][j][k-1] == INT_MAX:
                            continue
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
                if dp[i][j][K] != INT_MAX:
                    dp[i][j][1] = dp[i][j][K] +  presum[j] - presum[i] + stones[i]
        return dp[0][L-1][1]