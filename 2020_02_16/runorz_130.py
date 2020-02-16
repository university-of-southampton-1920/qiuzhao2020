class Solution:
    def find_connected(self, board, visited, x, y):
        connected = list()
        connected.append([x,y])
        visited[x][y] = True
        if x-1 >= 0 and visited[x-1][y] == False and board[x-1][y] == 'O':
            connected = connected + self.find_connected(board, visited, x-1, y)
        if x+1 < len(board) and visited[x+1][y] == False and board[x+1][y] == 'O':
            connected = connected + self.find_connected(board, visited, x+1, y)
        if y+1 < len(board[0]) and visited[x][y+1] == False and board[x][y+1] == 'O':
            connected = connected + self.find_connected(board, visited, x, y+1)
        if y-1 >= 0 and visited[x][y-1] == False and board[x][y-1] == 'O':
            connected = connected + self.find_connected(board, visited, x, y-1)
        return connected

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = list()
        for row in board:
            visited_row = list()
            for column in row:
                visited_row.append(False)
            visited.append(visited_row)
        
        groups = list()
        for rindex, row in enumerate(board):
            for cindex, column in enumerate(row):
                if column == 'O' and visited[rindex][cindex] == False:
                    groups.append(self.find_connected(board, visited, rindex, cindex))
                visited[rindex][cindex] = True
        print(groups)
        valid = list()
        for i in range(len(groups)):
            valid.append(True)
        for i in range(len(groups)):
            for position in groups[i]:
                if position[0] == len(board)-1 or position[1] == len(board[0])-1 or 0 in position:
                    valid[i] = False
            
        print(valid)
        for i in range(len(groups)):
            if valid[i] == True:
                for position in groups[i]:
                    board[position[0]][position[1]] = 'X'
