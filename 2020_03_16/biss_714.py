class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [0 for i in range(len(prices))]
        no = [0 for i in range(len(prices))]
        hold[0] = -prices[0]
        res = 0
        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], no[i-1] - prices[i])
            no[i] = max( hold[i-1]+prices[i]-fee, no[i-1] )
            res = max(hold[i], no[i])
        return res