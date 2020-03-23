class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        flag = True
        if s1 == "" and s2 == "":
            if s3 != "":
                flag = False
            else:
                flag = True
        
        s1 = "$" + s1
        s2 = "$" + s2
        s3 = "$$" + s3
        dp = [[0 for i in range(len(s2) )] for j in range(len(s1))]
        dp[0][0] = 1 if flag else 0
        for i in range(1, len(s1)):
            if s1[i] == s3[i+1]:
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(s2)):
            if s2[i] == s3[i+1]:
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s3[i+j+1] == s1[i]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if s3[i+j+1] == s2[j]:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        for i in dp:
            print(i)
        return dp[len(s1)-1][len(s2)-1] == 1


# aabcc
# dbbca
# aadbb     baccc
# if s1[i+j+1] == s1[i]:
#     dp[i][j] |= dp[i-1][j]

# if s[i+j+1] == s2[j]:
#     dp[i][j] |= 