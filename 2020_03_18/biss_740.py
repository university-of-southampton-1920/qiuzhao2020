class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        M = max(nums) 
        s = [0 for i in range(M+1)]
        for n in nums:
            s[n] += n
        dp = [0 for i in range(M+1)]
        dp[1] = s[1]
        for v in range(2, M+1):
            dp[v] = max(dp[v-2] + s[v], dp[v-1])
        return dp[M]