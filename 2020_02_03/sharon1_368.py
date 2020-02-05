class Solution:
    def largestDivisibleSubset(self, nums):

        if not nums: return []
        N = len(nums)
        nums.sort()
        dp = [0] * N
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]
