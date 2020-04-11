class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = list()
        n.append(1)
        for e in nums:
            if e > 0:
                n.append(e)
        n.append(1)
        dp = [[-1 for _ in range(len(n))] for _ in range(len(n))]
        return self.burst(n, dp, 0, len(n)-1)
    
    def burst(self, n, dp, left, right):
        if left+1 == right:
            return 0
        if dp[left][right] >= 0:
            return dp[left][right]
        res = 0
        for i in range(left+1, right):
            res = max(res, n[left]*n[i]*n[right] + self.burst(n,dp,left, i) + self.burst(n, dp, i, right))
        dp[left][right] = res
        return res
