class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 最优子结构
        # 重复子问题
        # 无后效性
        # 多重背包
        # 举例子
        dp = [0 for i in range(target+1)]
        dp[0] = 1 
        for j in range(1, target+1):
            for i in range(len(nums)):
                if j - nums[i] < 0:
                    continue
                dp[j] += dp[j - nums[i]]
        return dp[-1]