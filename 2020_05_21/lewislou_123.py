class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1:
            return 0
        dp1,dp2 = [0]*n,[0]*n
        l_min,l_max = prices[0],prices[-1]
        for i in range(1,n):
            if prices[i] < l_min:
                l_min = prices[i]
            dp1[i] = max(dp1[i-1],prices[i]-l_min)
        for j in range(n-2,-1,-1):
            if prices[j] > l_max:
                l_max = prices[j]
            dp2[j] = max(dp2[j+1],l_max-prices[j])
        result = 0
        for a in range(n-1):
            result = max(result,dp1[a]+dp2[a])
        return result