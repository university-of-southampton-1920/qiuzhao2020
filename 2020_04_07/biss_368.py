class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [[1, -1] for i in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = j
                        res = max(res, dp[i][0])
        s = []
        for i in range(len(nums)):
            if dp[i][0] == res:
                while i != -1:
                    s.append(nums[i])
                    i = dp[i][1]
                break
        return s