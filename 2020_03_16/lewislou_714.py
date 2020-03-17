class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prev_sell = 0
        prev_buy = -prices[0]
        profit = 0
        for p in prices[1:]:
            prev_buy = max(prev_sell - p, prev_buy)
            prev_sell =     max(prev_buy + p-fee, prev_sell)

        return prev_sell