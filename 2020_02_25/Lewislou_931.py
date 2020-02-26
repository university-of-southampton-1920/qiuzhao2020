class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                A[i][j] += min(A[i-1][max(j-1,0):j+2])  ##当前值加上前面所有可选值的最小值
        return min(A[-1])