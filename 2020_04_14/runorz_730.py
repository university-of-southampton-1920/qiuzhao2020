class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
        for i in range(len(S)):
            dp[i][i] = 1
        
        for step in range(1, len(S)):
            for i in range(len(S)):
                if i+step >= len(S):
                    break
                else:
                    if S[i] == S[i+step]:
                        left = i+1
                        right = i+step-1
                        while left <= right and S[left] != S[i]:
                            left += 1
                        while left <= right and S[right] != S[i+step]:
                            right -= 1
                        if left > right:
                            dp[i][i+step] = dp[i+1][i+step-1] * 2 + 2
                        if left == right:
                            dp[i][i+step] = dp[i+1][i+step-1] * 2 + 1
                        if left < right:
                            dp[i][i+step] = dp[i+1][i+step-1] * 2 - dp[left+1][right-1]
                    else:
                        dp[i][i+step] = dp[i+1][i+step] + dp[i][i+step-1] - dp[i+1][i+step-1]
                dp[i][i+step] = dp[i][i+step] + 1000000007 if dp[i][i+step] < 0 else dp[i][i+step] % 1000000007
        return dp[0][-1]
