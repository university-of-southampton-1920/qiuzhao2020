class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
        '''
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [0 for i in range(n+1)]
        dp[1] = nums[1]
        for i in range(n):
            val = nums[i]
            dp[i+1] = max(dp[i], dp[i-1] + val)
        return dp[-1]

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         pp = nums[0]
#         p = nums[1]
#         res = max(pp, p)
#         for i in range(2, len(nums)):
#             tmp = pp + nums[i]
#             pp = max(pp, p)
#             p = tmp
#             res = max(res, p, pp)
#         return res
#