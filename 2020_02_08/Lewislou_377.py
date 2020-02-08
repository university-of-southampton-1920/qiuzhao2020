class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
	    dp = [1]+ [0]*target
	    for i in range(1,target+1):
		    dp[i]=sum(dp[i-j] for j in nums if i-j>=0)
	    return dp[-1]
        