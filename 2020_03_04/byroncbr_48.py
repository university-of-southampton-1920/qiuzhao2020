"""
Name: byroncbr_48.py
Author: bangrenc
Time: 4/3/2020 9:10 AM
"""

def rotate(matrix):
    matrix = list(reversed(matrix))
    for i in range(len(matrix)):
        for j in range(i+1 , len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    return matrix

if __name__ == '__main__':
    matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    result = rotate(matrix)
    print(result)




