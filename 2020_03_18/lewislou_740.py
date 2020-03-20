class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        nums_sort = sorted(nums)
        max_num = nums_sort[-1]
        result = 0
        value = [0]*(max_num+1)
        dp = value
        for num in nums_sort:
            value[num] += num
        dp[0] = 0
        dp[1] = value[1]
        dp[2] = max(value[1],value[2])
        for i in range(3, max_num+1):
            dp[i] = max(value[i]+dp[i-2],dp[i-1])
            result = max(result,dp[i])
        return result
        
        
        