class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        maximal = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]: maximal = 1         

        for a in range(1,n):
            for b in range(1,m):
                if matrix[a-1][b-1] and matrix[a][b-1] and matrix[a-1][b] and matrix[a][b]:
                    matrix[a][b] = min(matrix[a-1][b-1],matrix[a][b-1],matrix[a-1][b])+1
                    if matrix[a][b] > maximal: maximal = matrix[a][b]

        return maximal**2
        