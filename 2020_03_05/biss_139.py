class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for i in range(len(s))]
        d = dict()
        for w in wordDict:
            d[w] = 1
        
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if j == 0 and s[j:i+1] in d:
                    dp[i] = 1
                elif dp[j] == 1 and s[j+1:i+1] in d:
                    dp[i] = 1
                    break
        if dp[len(s) - 1] == 1:
            return True
        return False