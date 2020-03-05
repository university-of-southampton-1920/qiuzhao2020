class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False for _ in range(len(s)+1)]
        f[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[len(s)]
