class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        minprice = float('inf')

        for i in range(n):
            if prices[i]<minprice:
                minprice = prices[i]
            elif (prices[i]-minprice)>ans:
                ans = prices[i]-minprice
        return ans
                