class Solution:
    count = 0
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        Solution.count = 0
        def calculate(nums,i,sum,S):
            if i == len(nums):
                if sum==S:
                    Solution.count=Solution.count+1
            else:
                calculate(nums,i+1,sum+nums[i],S)
                calculate(nums,i+1,sum-nums[i],S)
        calculate(nums,0,0,S)
        return Solution.count
		
		
#Dynamic programming
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [[0 for i in range(2001)] for j in range(len(nums))]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1
        if(sum(nums) < S):
            return 0
        for i in range(1,len(nums)):
            for sum1 in range(-1000,1000):
                if dp[i-1][sum1+1000] > 0:
                    dp[i][nums[i]+1000+sum1] += dp[i-1][sum1+1000]
                    dp[i][-nums[i]+1000+sum1] += dp[i-1][sum1+1000]
        return dp[len(nums)-1][S+1000]
##1-D danymic programming
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [0 for i in range(2001)]
        dp[nums[0]+1000] = 1
        dp[-nums[0]+1000] += 1
        if(sum(nums) < S):
            return 0
        for i in range(1,len(nums)):
            next = [0 for i in range(2001)]
            for sum1 in range(-1000,1000):
                if dp[sum1+1000] > 0:
                    next[nums[i]+1000+sum1] += dp[sum1+1000]
                    next[-nums[i]+1000+sum1] += dp[sum1+1000]
            dp = next
        return dp[S+1000]