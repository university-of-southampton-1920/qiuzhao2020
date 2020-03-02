class Solution:  # donot finish because of the 0 element corners case
    def splitArraySameAverage(self, A: List[int]) -> bool:
        all_sum = sum(A)
        L = len(A)
        dp = [[0 for i in range(all_sum+1)] for j in range(len(A)) ]
        # initialization
        dp[0][A[0]] = 1
        
        # cal dp
        for i in range(1, len(A)):
            for v in range(1, all_sum+1):
                if v - A[i] >= 0:
                    dp[i][v] = dp[i-1][v-A[i]]+1 if dp[i-1][v-A[i]] > 0 or v-A[i] == 0 else dp[i-1][v]
                    if dp[i][v] == len(A) or dp[i][v] == 0:
                        continue  # avoid dividing by 0 
                    up_avg = v / dp[i][v]
                    down_avg = (all_sum - v) / (L - dp[i][v] )
                    if up_avg == down_avg:
                        for k in dp:
                            print(k)
                        print(up_avg)
                        print(down_avg)
                        return True
        for k in dp:
            print(k)
        return False
        