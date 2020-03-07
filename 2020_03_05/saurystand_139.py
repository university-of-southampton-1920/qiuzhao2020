class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         if s is None or len(s) == 0: return False
#         n = len(s)
#         dp = [False] * n
#         for i in range(n):
#             for j in range(i, n):
#                 sub = s[i:j+1]
#                 #print(sub)
#                 if sub in wordDict and dp[i]:
#                     dp[j+1] = True
                    
#         return dp[-1]

        # maxw = 0
        # for s in wordDict:
        #     maxw = max(maxw, len(s))
        # slen = len(s)
        # dp = [False] * (slen + 1)
        # dp[0] = True
        # for i in range(slen + 1):
        #     start = max(1, i - maxw)
        #     for j in range(start, i+1):
        #         if dp[j-1] and s[j-1:i] in wordDict:
        #             dp[i] = True
        #             break
        # return dp[slen]
        slen = len(s)
        dp = [False] * slen
        for i in range(slen):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i] = True
        return dp[-1]


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [0 for i in range(len(s))]
#         d = dict()
#         for w in wordDict:
#             d[w] = 1
        
#         for i in range(len(s)):
#             for j in range(i, -1, -1):
#                 if j == 0 and s[j:i+1] in d:
#                     dp[i] = 1
#                 elif dp[j] == 1 and s[j+1:i+1] in d:
#                     dp[i] = 1
#                     break
#         if dp[len(s) - 1] == 1:
#             return True
#         return False