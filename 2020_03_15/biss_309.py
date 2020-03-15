class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        L = len(prices)
        hold = [0 for i in range(L)]
        no = [0 for i in range(L)]
        cool = [0 for i in range(L)]
        hold[0] = -prices[0]
        no[0] = 0
        cool[0] = -10**8
        res = 0
        for i in range(1, L):
            hold[i] = max(no[i-1]-prices[i], hold[i-1])
            no[i] = max(cool[i-1], no[i-1])
            cool[i] = hold[i-1] + prices[i]
            res = max(res, hold[i], no[i], cool[i])
        return res