import numpy as np
class Solution:
  def minFallingPathSum(self, A) -> int:
    dp = np.zeros((len(A),len(A)))
    # dp[0], dp[len(A)+1], dp[:,0], dp[:,len(A)+1] = 101, 101, 101, 101
    # for cindex in range(len(A), 0, -1):
    #   dp[len(A)][cindex] = A[len(A)-1][cindex-1]
    for cindex in range(len(A)):
      dp[len(A)-1,cindex] = A[len(A)-1][cindex]
    # for rindex in range(len(A)-1, 0, -1):
    #   for cindex in range(1, len(A)+1, 1):
    #     dp[rindex][cindex] = A[rindex-1][cindex-1] + min(dp[rindex+1][cindex-1], dp[rindex+1][cindex], dp[rindex+1][cindex+1])
    for rindex in range(len(A)-2, -1, -1):
      for cindex in range(len(A)):
        minimum = 99999999
        for c in range(len(A)):
          if dp[rindex+1][c] < minimum and c!=cindex:
            minimum = dp[rindex+1][c]
        dp[rindex][cindex] = minimum + A[rindex][cindex]
    print(dp)
    return int(np.min(dp[0,0:len(A)]))
