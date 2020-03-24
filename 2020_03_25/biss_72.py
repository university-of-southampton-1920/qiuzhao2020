class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = "$" + word1
        w2 = "$" + word2
        dp = [[0 for i in range(len(w2))] for j in range(len(w1))]
        for i in range(1, len(w2)):
            dp[0][i] = dp[0][i-1] + 1
        for i in range(1, len(w1)):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, len(w1)):
            for j in range(1, len(w2)):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[len(w1)-1][len(w2)-1]
    
# if word1[i] == word2[j]:
#     dp[i][j] = dp[i-1][j-1]
# else:
#     # insert
#     # exection
#     # execution
    
#     # remove
#     # rorse
#     # rose
    
#     # replace
#     # horse
#     # rorse
#     dp[i-1][j-1] + 1
#     dp[i-1][j]+1 # delete
#     dp[i][j-1]+1 # insert