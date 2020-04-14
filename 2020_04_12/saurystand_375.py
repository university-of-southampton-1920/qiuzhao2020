class Solution:
    def getMoneyAmount(self, n: int) -> int:
        '''
        For each number x in range[i~j]
        we do: result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
        --> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
        then we get DP([i~j]) = min{xi, ... ,xj}
        --> // this min makes sure that you are minimizing your cost.
        '''
        dp = [[0]*(n+1) for _ in range(n+1)]
        for j in range(2, n+1):
            for i in range(j-1, 0, -1):
                globalmin = float('inf')
                for k in range(i+1, j):
                    localmax = max(dp[i][k-1], dp[k+1][j]) + k
                    globalmin = min(localmax, globalmin)
                dp[i][j] = i if i+1 == j else globalmin
        return dp[1][n]