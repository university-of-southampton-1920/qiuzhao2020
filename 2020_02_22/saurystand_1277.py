class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
'''
Store dp state and add to count in same nested for loop.
DP state to store: find min of (i-1,j), (i,j-1), (i-1,j-1) and add one.
for example:
1 1
1 1 <---this should be 2 because it's both a 2x2 square and a 1x1 square
another bigger example:

BEFORE
[0,1,1,1]
[1,1,1,1]
[0,1,1,1]
AFTER
[0,1,1,1]
[1,1,2,2]
[0,1,2,3]
'''
        count = 0
        m,m0 = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(m0):
                if i != 0 and j != 0 and matrix[i][j] != 0:
                    minf = min(min(matrix[i-1][j-1], matrix[i-1][j]), matrix[i][j-1])
                    matrix[i][j] = minf + 1
                count += matrix[i][j]
        return count