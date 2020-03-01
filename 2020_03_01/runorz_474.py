class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        res = 0
        for string in strs:
            zeros = string.count('0')
            ones = string.count('1')
            
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    if dp[i-zeros][j-ones] >=0:
                        dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
                        res = max(res, dp[i][j])
        return res
