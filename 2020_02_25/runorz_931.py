import numpy as np
class Solution:
  def minFallingPathSum(self, A) -> int:
    dp = np.zeros((len(A)+2,len(A)+2))
    dp[0], dp[len(A)+1], dp[:,0], dp[:,len(A)+1] = 101, 101, 101, 101
    for cindex in range(len(A), 0, -1):
      dp[len(A)][cindex] = A[len(A)-1][cindex-1]
    for rindex in range(len(A)-1, 0, -1):
      for cindex in range(1, len(A)+1, 1):
        dp[rindex][cindex] = A[rindex-1][cindex-1] + min(dp[rindex+1][cindex-1], dp[rindex+1][cindex], dp[rindex+1][cindex+1])
    return int(np.min(dp[1,1:len(A)+1]))
