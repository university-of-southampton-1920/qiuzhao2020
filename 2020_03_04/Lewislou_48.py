class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        last = len(matrix)-1
        for r in range(last):
            for c in range(r, last-r):
                matrix[r][c], matrix[last-c][r], matrix[last-r][last-c], matrix[c][last-r] = matrix[last-c][r], matrix[last-r][last-c], matrix[c][last-r], matrix[r][c]