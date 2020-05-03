class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        text = "$" + text
        dp = [[0 for i in range(len(text))] for j in range(len(text))]
        dp[0][0] = 0
        res = dict()
        for i in range(1, len(text)):
            for j in range(i+1, len(text)):
                if text[i] == text[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if j - dp[i][j] <= i:
                    l = j-i-1
                    res[text[i-l:j+1]] = 1
        return len(res)