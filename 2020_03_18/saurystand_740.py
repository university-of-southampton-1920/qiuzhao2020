class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0] * 10001
        for n in nums:
            count[n] += n
        dp = [0] * 10003
        for i in range(10000, -1, -1):
            dp[i] = max(count[i] + dp[i+2], dp[i+1])
        return dp[0]


# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         M = max(nums)
#         s = [0 for i in range(M+1)]
#         for n in nums:
#             s[n] += n
#         dp = [0 for i in range(M+1)]
#         dp[1] = s[1]
#         for v in range(2, M+1):
#             dp[v] = max(dp[v-2] + s[v], dp[v-1])
#         return dp[M]