from collections import Counter
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for i in range(len(nums))] # length, num
        maxll = 1
        for i in range(1, len(nums)):
            c = Counter()
            maxl = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxl = max(maxl, dp[j][0])
                    c[dp[j][0]] += dp[j][1]
            dp[i][0] = maxl + 1
            dp[i][1] = max(c[maxl], dp[i][1])
            maxll = max(maxll, dp[i][0])
        res = 0
        print(dp)
        for d in dp:
            if d[0] == maxll:
                res += d[1]
        return res