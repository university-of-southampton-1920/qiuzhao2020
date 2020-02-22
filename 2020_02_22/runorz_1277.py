class Solution:
    def find_square(self, matrix, border):
        length_zero = len(matrix)
        length_one = len(matrix[0])
        mid = int(len(border)/2)
        temp_border = list()
        for i in range(len(border)):
            if i == mid:
                if border[i][0]+1 < length_zero and border[i][1]+1 < length_one:
                    temp_border.append([border[i][0]+1, border[i][1]])
                    temp_border.append([border[i][0]+1, border[i][1]+1])
                    temp_border.append([border[i][0], border[i][1]+1])
            if i < mid:
                if border[i][0] + 1 < length_zero:
                    temp_border.append([border[i][0]+1, border[i][1]])
            if i > mid:
                if border[i][1] + 1 < length_one:
                    temp_border.append([border[i][0], border[i][1]+1])
        for e in temp_border:
            if matrix[e[0]][e[1]] == 0:
                return 1
        if len(temp_border) == len(border)+2:
            return 1 + self.find_square(matrix,temp_border)
        else:
            return 1
    
    def countSquares(self, matrix: List[List[str]]) -> int:
        result = 0
        for rindex, row in enumerate(matrix):
            for cindex, col in enumerate(row):
                if col == 1:
                    result = result + self.find_square(matrix, [[rindex, cindex]])
        return result
