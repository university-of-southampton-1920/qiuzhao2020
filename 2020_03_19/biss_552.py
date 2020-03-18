class Solution:
    def checkRecord(self, n: int) -> int:
        dp00, dp01, dp02, dp10, dp11, dp12 = 1, 0, 0, 0, 0, 0
        M = 10**9 + 7
        for i in range(1, n+1):
            dp00_ = (dp00 + dp01 + dp02) % M
            dp01_ = dp00
            dp02_ = dp01
            dp10_ = (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % M
            dp11_ = dp10
            dp12_ = dp11
            dp00, dp01, dp02, dp10, dp11, dp12 = dp00_, dp01_, dp02_, dp10_, dp11_, dp12_
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % M
    

# dp0[i] = dp0[i-1]*2
# dp1[i] = dp0[i-1] + dp1[i-1] * 2

# # ------- #
# dp0[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1]) * 2
# dp1[i] = dp0[i-1] 
# dp2[i] = dp1[i-1]

# # ------- #
# dp00[i] = dp00[i-1] + dp01[i-1] + dp02[i-1]  # no appearance of A, ending with no L
# dp01[i] = dp00[i-1]  # no appearance of A, ending with one L
# dp02[i] = dp01[i-1]  # no appearance of A, ending with two L
# dp10[i] = dp00[i-1] + dp01[i-1] + dp02[i-1] + dp10[i-1] + dp11[i-1] + dp12[i-1]   # appearance of A, ending with no L
# dp11[i] = dp10[i-1]  # appearance of A, ending with one L
# dp12[i] = dp11[i-1]  # appearance of A, ending with two L