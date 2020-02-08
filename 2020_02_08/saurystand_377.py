class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        dp = [0] * (target + 1)
        #dp = [0 for i in range(target + 1)]
        # full dp
        dp[0] = 1
        numLengh = len(nums)
        for i in range(1, target + 1):
            for j in range(numLengh):
                if i - nums[j] >= 0:
                    dp[i] = dp[i] + dp[i - nums[j]]
        
        return dp[target]