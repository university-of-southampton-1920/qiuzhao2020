from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for k in range(n+1)] for j in range(m+1)]
        s_arr = []
        for s in strs:
            s_arr.append( Counter(s) )
        # initialization
        for m1 in range(m+1):
            for n1 in range(n+1):
                if m1 - s_arr[0]["0"] < 0 or n1 - s_arr[0]["1"] < 0:
                    continue
                dp[m1][n1] = 1
        
        for i in range(1, len(strs)):
            t = [tt.copy() for tt in dp]
            for m1 in range(m+1):
                for n1 in range(n+1):
                    if m1 - s_arr[i]["0"] < 0 or n1 - s_arr[i]["1"] < 0:
                        continue
                    else:
                        t[m1][n1] = max(dp[m1-s_arr[i]["0"]][n1-s_arr[i]["1"]] + 1, dp[m1][n1])
            dp = t
            # print(s_arr[i])
            # for pp in dp:
            #     print(pp)
            # print()

        return dp[m][n]