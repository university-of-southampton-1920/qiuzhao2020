class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        https://leetcode.com/problems/rotate-image/discuss/18895/Clear-Java-solution
        https://leetcode.com/problems/rotate-image/discuss/235478/Success%3ASimple-java-solution-beats-100-of-online-submission-explained-in-detail
        """
        n = len(matrix)
        nn = int ((n+1)/2)
        for i in range(nn):
            for j in range(i,n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp



# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         for i in range( int(len(matrix) /2) ):
#             for j in range(len(matrix[0])):
#                 matrix[i][j], matrix[len(matrix)-i-1][j] = matrix[len(matrix)-i-1][j], matrix[i][j]
        
#         for i in range(len(matrix)):
#             for j in range(i, len(matrix[0])):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         
