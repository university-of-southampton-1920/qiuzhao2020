class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        if k > int(len(prices)/2):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        
        dp_no = [-10**7 for i in range(k+1)]
        dp_hold = [-10**7 for i in range(k+1)]
        
        dp_no[0] = 0
        dp_hold[0] = -prices[0]
        res = 0
        for i in range(len(prices)):
            dp_no_old = dp_no[:]
            dp_hold_old = dp_hold[:]
            for j in range(1, k+1):
                dp_hold[j] = max(dp_hold_old[j], dp_no_old[j] - prices[i])
                dp_no[j] = max(dp_no_old[j], dp_hold_old[j-1] + prices[i])
                res = max(res, dp_hold[j], dp_no[j])

            dp_hold[0] = max(dp_hold_old[0], -prices[i])
        return res