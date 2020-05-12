from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for i in range(len(nums))]
        q = deque()
        res = -10**8
        for i in range(len(nums)):
            while len(q) > 0 and i-q[0]>k:
                q.popleft()
            dp[i] = nums[i]
            if len(q) > 0:
                dp[i] = max(dp[i], dp[q[0]] + nums[i])
            while len(q)>0 and dp[i] > dp[q[-1]]:
                q.pop()
            q.append(i)
            res = max(res, dp[i])
        return res