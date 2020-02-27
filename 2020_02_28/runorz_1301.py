class Solution:
    def findPaths(self, board, dp, x, y):
        if board[x][y] == 'E':
            return [0,1]
        up_left_diag = [None for _ in range(3)]
        if x-1 >= 0 and board[x-1][y]!='X':
            if dp[x-1][y] != None:
                up_left_diag[0] = dp[x-1][y]
            else:
                up_left_diag[0] = self.findPaths(board, dp, x-1, y)
        if y-1 >= 0 and board[x][y-1]!='X':
            if dp[x][y-1] != None:
                up_left_diag[1] = dp[x][y-1]
            else:
                up_left_diag[1] = self.findPaths(board, dp, x, y-1)
        if x-1 >=0 and y-1 >= 0 and board[x-1][y-1] != 'X':
            if dp[x-1][y-1] != None:
                up_left_diag[2] = dp[x-1][y-1]
            else:
                up_left_diag[2] = self.findPaths(board, dp, x-1, y-1)
        max_value = -1
        max_times = 0
        for element in up_left_diag:
            if element != None:
                if element[0] > max_value:
                    max_value = element[0]
        for element in up_left_diag:
            if element != None:
                if element[0] == max_value:
                    max_times += element[1]
        if max_times == 0:
            dp[x][y] = [0,0]
            return [0,0]
        dp[x][y] = [int(board[x][y])+max_value, max_times]
        return [int(board[x][y])+max_value, max_times]

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        dp = [[None for _ in range(len(board))] for _ in range(len(board))]
        x = len(board)-1
        y = len(board)-1
        up_left_diag = [None for _ in range(3)]
        if x-1 >= 0 and board[x-1][y]!='X':
            up_left_diag[0] = self.findPaths(board, dp, x-1, y)
        if y-1 >= 0 and board[x][y-1]!='X':
            up_left_diag[1] = self.findPaths(board, dp, x, y-1)
        if x-1 >=0 and y-1 >= 0 and board[x-1][y-1] != 'X':
            up_left_diag[2] = self.findPaths(board, dp, x-1, y-1)
        max_value = -1
        max_times = 0
        for element in up_left_diag:
            if element != None:
                if element[0] > max_value:
                    max_value = element[0]
        for element in up_left_diag:
            if element != None:
                if element[0] == max_value:
                    max_times += element[1]
        print(dp[-1][0])
        print(dp[-1][1])
        print(dp[-2][0])
        print(dp[-2][1])
        if max_times == 0:
            return [0,0]
        return [max_value, max_times%(10**9+7)]
