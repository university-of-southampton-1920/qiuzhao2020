class Solution:
  def __init__(self):
    self.M = 1000000007
  def find(self, m, n, N, i, j, memo) -> int:
    if i == m or j == n or i < 0 or j < 0:
      return 1
    if N==0:
      return 0
    if memo[i][j][N] >= 0:
      return memo[i][j][N]
    memo[i][j][N] = (self.find(m,n,N-1,i-1,j,memo) + self.find(m,n,N-1,i+1,j,memo)+ self.find(m,n,N-1,i,j-1,memo) + self.find(m,n,N-1,i,j+1,memo))%self.M
    return memo[i][j][N]
    
  def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
    memo = [[[-1 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
    return self.find(m,n,N,i,j,memo)
