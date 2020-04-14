class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for j in range(2,n+1):
            for i in range(j-1,0,-1):
                global_min = float('inf')
                for k in range(i+1,j):
                    local_max = k + max(dp[i][k-1], dp[k+1][j])  
                    #[1,2,3,4] k = 2, dp[1][1] = 0 dp[3][4] = 3, so local_max = 2 + max(0,3) = 5
                    #[1,2,3,4] k = 3, dp[1][2] = 1 dp[4][4] = 0, so local_max = 3 + max(0,1) = 4
                    global_min = min(global_min, local_max)
                    #global_min = min(4,5)
                dp[i][j] = i if i+1 ==j else global_min  #[1,2]
        return dp[1][n]