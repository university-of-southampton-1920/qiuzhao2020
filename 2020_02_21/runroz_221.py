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
            if matrix[e[0]][e[1]] == '0':
                return len(border)
        if len(temp_border) == len(border)+2:
            return len(border) + self.find_square(matrix,temp_border)
        else:
            return len(border)
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        for rindex, row in enumerate(matrix):
            for cindex, col in enumerate(row):
                if col == '1':
                    temp = self.find_square(matrix, [[rindex, cindex]])
                    if result < temp:
                        result = temp
        return result
