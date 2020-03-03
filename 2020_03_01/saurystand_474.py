class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0] * (n+1)] * (m+1)
#         for s in strs:
#             count_len = self.countS(s)
#             for i in range(m,count_len[0],-1,-1):
#                 for j in range(n, count_len[1],-1,-1):
#                     dp[i][j] = max(1+dp[i-count_len[0]][j-count_len[1]], dp[i][j])
#         return dp[m][n]
            
            
#     def countS(self, string):
#         result = [0] * 2
#         for i in range(len(string)):
#             print(string[i])
#             result[string[i] - '0'] += 1
#         return result
        dp = [[0 for k in range(n+1)] for j in range(m+1)]
        ms = [0] * len(strs)
        ns = [0] * len(strs)
        for i in range(len(strs)):
            s = strs[i]
            for j in range(len(s)):
                c = s[j]
                if c == '0':
                    ms[i] += 1
                else:
                    ns[i] += 1
        
        for i in range(len(ms)):
            for mm in range(m,ms[i]-1,-1):
                for nn in range(n,ns[i]-1,-1):
                    dp[mm][nn] = max(dp[mm][nn], dp[mm-ms[i]][nn-ns[i]] + 1)
        return dp[m][n]


# from collections import Counter
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0 for k in range(n+1)] for j in range(m+1)]
#         s_arr = []
#         for s in strs:
#             s_arr.append( Counter(s) )
#         # initialization
#         for m1 in range(m+1):
#             for n1 in range(n+1):
#                 if m1 - s_arr[0]["0"] < 0 or n1 - s_arr[0]["1"] < 0:
#                     continue
#                 dp[m1][n1] = 1
        
#         for i in range(1, len(strs)):
#             t = [tt.copy() for tt in dp]
#             for m1 in range(m+1):
#                 for n1 in range(n+1):
#                     if m1 - s_arr[i]["0"] < 0 or n1 - s_arr[i]["1"] < 0:
#                         continue
#                     else:
#                         t[m1][n1] = max(dp[m1-s_arr[i]["0"]][n1-s_arr[i]["1"]] + 1, dp[m1][n1])
#             dp = t
#             # print(s_arr[i])
#             # for pp in dp:
#             #     print(pp)
#             # print()

#         return dp[m][n]