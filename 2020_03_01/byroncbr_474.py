"""
Name: byroncbr_474.py
Author: bangrenc
Time: 2/3/2020 9:43 AM
"""

def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for x in range(m + 1)]
    for s in strs:
        zero, one = s.count('0'), s.count('1')
        for x in range(m, zero - 1, -1):
            for y in range(n, one - 1, -1):
                dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
    return dp[m][n]

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    result = findMaxForm(strs,m,n)
    print(result)




