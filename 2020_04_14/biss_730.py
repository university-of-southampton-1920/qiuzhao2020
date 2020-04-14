class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        dp = [[0 for i in range(len(S))] for j in range(len(S))]
        next_c = [[10**8 for j in range(4)] for i in range(len(S))]
        pre_c = [[-10**8 for j in range(4)] for i in range(len(S))]
        M = 10**9 + 7
        for c in range(4):
            i = 0
            for j in range(len(S)):
                if ord(S[j]) - ord("a") != c:
                    continue
                while i<=j:
                    next_c[i][c] = j
                    i+=1
        for c in range(4):
            i = len(S) - 1
            for j in range(len(S)-1, -1, -1):
                if ord(S[j]) - ord("a") != c:
                    continue
                while i>=j:
                    pre_c[i][c] = j
                    i-=1
        for i in range(len(S)):
            dp[i][i] = 1
        for i in range(len(S)-1):
            dp[i][i+1] = 2
        for l in range(2, len(S)):
            for i in range(len(S)-l):
                j = i+l
                for c in range(4):
                    p = next_c[i][c]
                    q = pre_c[j][c]
                    if p < q:
                        dp[i][j] += dp[p+1][q-1] + 1
                    if next_c[i][c] <= j:
                        dp[i][j] += 1
                    dp[i][j] %= M
        return dp[0][len(S)-1]