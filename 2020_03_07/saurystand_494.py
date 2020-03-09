class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # nlen = len(nums)
        # sumN = 0
        # for i in range(nlen):
        #     sumN += nums[i]
        # if S > sumN or (sumN + S) % 2 == 1:
        #     return 0
        # dp = [0] * (S + 1)
        # dp[0] = 1
        # subsetS = int((sumN + S) / 2)
        # for i in range(nlen):
        #     for j in range(subsetS, nums[i] +1, -1):
        #         dp[j] += dp[j-nums[i]]
        # return dp[S]
        dp = [{} for _ in range(len(nums))]
        if nums[0] == 0:
            dp[0] = {0:2}
        else:
            dp[0] = {nums[0] : 1, -nums[0] : 1}
        for i in range(1, len(nums)):
            current_hist = {}
            for k,v in dp[i-1].items():
                current_hist[k + nums[i]] = current_hist.get(k + nums[i], 0) + v
                current_hist[k - nums[i]] = current_hist.get(k-nums[i], 0) + v
            dp[i] = current_hist
        return dp[-1].get(S, 0)


# from collections import Counter
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         rsum = sum(nums)
#         dp = [Counter() for i in range(len(nums)+1)]
#         dp[0][0] = 1
#         nums = [0] + nums
#         for i in range(1, len(nums)):
#             for s in range(-rsum, rsum+1):
#                 dp[i][s+nums[i]] += dp[i-1][s]
#                 dp[i][s-nums[i]] += dp[i-1][s]
#         return dp[len(nums)-1][S]