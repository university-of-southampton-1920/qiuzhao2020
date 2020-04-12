import numpy as np
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.guess(dp, 1, n)
    
    def guess(self, dp, left, right):
        if left >= right:
            return 0
        if dp[left][right] > 0:
            return dp[left][right]
        res = np.inf
        for i in range(left, right+1):
            temp = i + max(self.guess(dp,left,i-1), self.guess(dp,i+1, right))
            res = min(res, temp)
        dp[left][right] = res
        return res
