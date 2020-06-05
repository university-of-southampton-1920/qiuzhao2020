class Solution:
    def __init__(self):
        self.res = []

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        top_left = [0, 0]
        bottom_right = [len(matrix)-1, len(matrix[0])-1]
        while top_left[0] < bottom_right[0] and top_left[1] < bottom_right[1]:
            self.helper(matrix, top_left, bottom_right)
            top_left[0] +=1
            top_left[1] +=1
            bottom_right[0]-=1
            bottom_right[1]-=1
        # width
        if top_left[0] == bottom_right[0]:
            for i in range(top_left[1], bottom_right[1]+1):
                self.res.append(matrix[top_left[0]][i])
        elif top_left[1] == bottom_right[1]:
            # deep
            for i in range(top_left[0], bottom_right[0]+1):
                self.res.append(matrix[i][top_left[1]])
        return self.res

    def helper(self, matrix, top_left, bottom_right):
        # top
        for i in range(top_left[1], bottom_right[1]):
            self.res.append(matrix[top_left[0]][i])
        # right
        for i in range(top_left[0], bottom_right[0]):
            self.res.append(matrix[i][bottom_right[1]])
        # bottom
        for i in range(bottom_right[1], top_left[1], -1):
            self.res.append(matrix[bottom_right[0]][i])
        # left
        for i in range(bottom_right[0], top_left[0], -1):
            self.res.append(matrix[i][top_left[1]])