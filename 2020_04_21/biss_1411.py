class Solution:
    def numOfWays(self, n: int) -> int:
        # 0: red, 1: yellow, 2: green
        mark = ["010", "012", "020", "021",
                "101", "102", "120", "121",
                "201", "202", "210", "212"]
        M = 10**9 + 7
        dp = [[0 for j in range(len(mark))] for i in range(n)]
        dp[0]  = [1 for i in range(len(mark))]
        for i in range(1, n):
            for cur in range(len(mark)):
                for pre in range(len(mark)):
                    if self.is_not_conflict(mark, cur, pre):
                        dp[i][cur] += dp[i-1][pre]
                dp[i][cur] %= M
        res = 0
        for i in range(len(mark)):
            res += dp[n-1][i]
        return res % M
    
    def is_not_conflict(self, mark, cur, pre):
        for i in range(3):
            if mark[cur][i] == mark[pre][i]:
                return False
        return True
                