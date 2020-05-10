class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0]*n
        diag1 = [0]*(2*n)
        diag2 = [0]*(2*n)
        self.result = 0
        def backTrack(y):
            if y==n:
                self.result+=1
            else:
                for x in range(n):
                    if (cols[x] or diag1[x+y] or diag2[x-y-1+n]): continue
                    cols[x],diag1[x+y],diag2[x-y-1+n]=1,1,1
                    backTrack(y+1)
                    cols[x],diag1[x+y],diag2[x-y-1+n] = 0,0,0
                        
        backTrack(0)
        return self.result
                        