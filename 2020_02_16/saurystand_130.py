class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R<=2 or C<=2:
            return
        queue = collections.deque()
        for r in range(R):
            queue.append((r, 0))
            queue.append((r, C - 1))

        for c in range(len(board[0])):
            queue.append((0, c))
            queue.append((R - 1, c))

        while queue:
            r, c = queue.popleft()
            print(r, c)
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = '*'
                queue.append((r-1, c))
                queue.append((r + 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

        for r in range(R):
            for c in range(C):
                if board[r][c] == '*':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if board == []:
#             return 
#         mark = dict()
        
#         for i in range(len(board[0]) ):
#             if board[0][i] == "O" and not ( (0, i) in mark) :
#                 self.dfs(board, mark, (0, i) )
#             if board[len(board)-1][i] == "O" and not( (len(board)-1, i) in mark):
#                 self.dfs(board, mark, (len(board)-1, i) )
        
#         for i in range(len(board)):
#             if board[i][0] == "O" and not ( (i, 0) in mark ):
#                 self.dfs(board, mark, (i, 0))
#             if board[i][len(board[0]) -1] == "O" and not( (i, len(board[0])-1) in mark ):
#                 self.dfs(board, mark, (i, len(board[0])-1) )
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == "X" or  (i, j) in mark:
#                     continue
#                 else:
#                     board[i][j] = "X" 
    
#     def dfs(self, arr, mark, pos):
#         if pos in mark:
#             return
#         mark[pos] = 1
#         for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             new_row = pos[0] + d[0]
#             new_col = pos[1] + d[1]
#             if 0<=new_row<len(arr) and 0<=new_col<len(arr[0]) and arr[new_row][new_col]=="O" and not ((new_row, new_col) in mark):
#                 self.dfs(arr, mark, (new_row, new_col))