class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        maximal = 1
        number = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] and matrix[i-1][j-1] and matrix[i][j-1] and matrix[i-1][j]:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + 1
                    if matrix[i][j] > maximal: maximal = matrix[i][j]
                
        for i in range(1,maximal+1):
            number += i*sum(row.count(i) for row in matrix)  
        
        return number
        