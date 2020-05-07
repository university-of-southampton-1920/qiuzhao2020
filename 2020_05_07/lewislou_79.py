class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0: return True # corner case
        if len(board[0]) == 0: return False # corner case
        nrow, ncol = len(board), len(board[0])
        def backtrack(i, j, pos, visit):
            if pos == len(word)-1: return True # end
            outcome = False # we only need one path that works
            if i>0 and not (i-1,j) in visit and board[i-1][j] == word[pos+1]: # up
                visit.add((i-1,j))
                outcome = outcome or backtrack(i-1, j, pos+1, visit)
                visit.remove((i-1,j))
            if j>0 and not (i,j-1) in visit and board[i][j-1] == word[pos+1]: # left
                visit.add((i,j-1))
                outcome = outcome or backtrack(i, j-1, pos+1, visit)
                visit.remove((i,j-1))
            if i<nrow-1 and not (i+1,j) in visit and board[i+1][j] == word[pos+1]: # down
                visit.add((i+1,j))
                outcome = outcome or backtrack(i+1, j, pos+1, visit)
                visit.remove((i+1,j))
            if j<ncol-1 and not (i,j+1) in visit and board[i][j+1] == word[pos+1]: # right
                visit.add((i,j+1))
                outcome = outcome or backtrack(i, j+1, pos+1, visit)
                visit.remove((i,j+1))
            return outcome
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    visit = set()
                    visit.add((i,j))
                    if backtrack(i,j,0,visit): return True
        return False