class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        n = sorted(nums)
        dp = [None for _ in range(len(n))]
        dp[0] = [n[0]]
        for i in range(1, len(n)):
            temp = [n[i]]
            for j in range(i):
                if n[i] % dp[j][-1] == 0 and len(dp[j])+1 > len(temp):
                    temp = dp[j] + [n[i]]
            dp[i] = temp
        res = []
        for e in dp:
            if len(e) > len(res):
                res = e
        return res
