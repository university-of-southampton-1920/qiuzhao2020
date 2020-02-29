class Solution:
    def pathsWithMaxScore(self, B: List[str]) -> List[int]:
        L, B, m = len(B), [list(b) for b in B], 10**9 + 7
        B[0][0], B[-1][-1], DP = '0', '0', [[(0,0) for _ in range(L)] for _ in range(L)]
        DP[-1][-1] = (0,1)
        for n in range(L-2,-1,-1):
            if B[L-1][n] == 'X': break
            DP[L-1][n] = (int(DP[L-1][n+1][0])+int(B[L-1][n]), 1)
        for n in range(L-2,-1,-1):
            if B[n][L-1] == 'X': break
            DP[n][L-1] = (int(DP[n+1][L-1][0])+int(B[n][L-1]), 1)
        for i,j in itertools.product(range(L-2,-1,-1),range(L-2,-1,-1)):
            if B[i][j] == 'X': continue
            M = max(DP[x][y][0] for x,y in [(i,j+1),(i+1,j+1),(i+1,j)])
            P = sum(DP[x][y][1] for x,y in [(i,j+1),(i+1,j+1),(i+1,j)] if DP[x][y][0]==M)
            DP[i][j] = (int(B[i][j])*(P>0) + M, P)
        return [DP[0][0][0], DP[0][0][1] % m]