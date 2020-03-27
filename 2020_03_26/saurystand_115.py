class Solution {
    public int numDistinct(String s, String t) {
        // array creation
        int[][] mem = new int[t.length()+1][s.length()+1];

        // filling the first row: with 1s
        for(int j=0; j<=s.length(); j++) {
            mem[0][j] = 1;
        }

        // the first column is 0 by default in every other rows but the first, which we need.

        for(int i=0; i<t.length(); i++) {
            for(int j=0; j<s.length(); j++) {
                if(t.charAt(i) == s.charAt(j)) {
                    mem[i+1][j+1] = mem[i][j] + mem[i+1][j];
                } else {
                    mem[i+1][j+1] = mem[i+1][j];
                }
            }
        }

        return mem[t.length()][s.length()];
    }
}


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#
#         dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
#         dp[0][0] = 1
#         # fill in first row
#         for i in range(len(s) + 1):
#             dp[i][0] = 1
#         #  the first column is 0 by default in every other rows but the first, which we need.
#         for i in range(1, len(s) + 1):
#             for j in range(1, len(t) + 1):
#                 if s[i - 1] == t[j - 1]:
#                     dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = dp[i - 1][j]
#         return dp[-1][-1]
