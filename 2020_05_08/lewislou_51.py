class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0]*n
        diag1 = [0]*(2*n)
        diag2 = [0]*(2*n)
        result = []
        def backTrack(y,grid=[]):
            if y==n:
                result.append(grid[:])
            else:
                for x in range(n):
                    if(cols[x] or diag1[x+y] or diag2[x-y-1+n]): continue
                    cols[x],diag1[x+y],diag2[x-y-1+n]=1,1,1
                    tempgrid = ['.']*n
                    tempgrid[x] = 'Q'
                    grid.append(''.join(tempgrid))
                    backTrack(y+1)
                    cols[x],diag1[x+y],diag2[x-y-1+n] = 0,0,0
                    grid.pop()
        backTrack(0)
        return result