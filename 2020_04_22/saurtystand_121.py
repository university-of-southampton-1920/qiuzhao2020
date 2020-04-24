class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv = 0
        minv = float('inf')
        for p in prices:
            if p < minv:
                minv = p
            elif p - minv > maxv:
                maxv = p - minv

        return maxv