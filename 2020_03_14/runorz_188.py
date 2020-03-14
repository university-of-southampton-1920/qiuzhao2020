class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)/2:
            return self.quick(k, prices)
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1,k+1):
            temp = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + temp)
                temp = max(temp, dp[i-1][j-1]-prices[j])
        return dp[k][len(prices)-1]
    
    def quick(self,k, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit+=prices[i] - prices[i-1]
        return profit
