class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]
    #         n = len(A)
#         dp = [0] * n
#         initMax = A[0]
#         for i in range(K):
#             if A[i] > initMax:
#                 initMax = A[i]
#             dp[i] = initMax * i

#         i = K
#         for i in range(n):
#             curr = 0
#             kinternalmax = A[i]
#             for j in range(1,K):
#                 # Keep track of the current maximum in the window [i-j+1, i].
#                 if A[i-j+1] > kinternalmax:
#                     kinternalmax = A[i-j+1]
#                 # cur is the candidate for the solution to memo[i] as we backtrack the K-1 window.
#                 curr = dp[i-j] + j *kinternalmax
#                 if curr > dp[i]:
#                     dp[i] = curr

#         return dp[-1]
