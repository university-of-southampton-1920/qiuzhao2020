from collections import Counter, defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [Counter() for i in range(len(key))] # [i][pos] : v
        c2i = defaultdict(list)
        for i in range(len(ring)):
            c2i[ring[i]].append(i)
        
        for cur_i in c2i[key[0]]:
            dp[0][cur_i] =  min( abs(cur_i - 0), len(ring)-abs(cur_i - 0) ) 
        
        for i in range(1, len(key)):
            for cur_i in c2i[key[i]]:
                dp[i][cur_i] = 10**8
                for pre_i in c2i[key[i-1]]:
                    dp[i][cur_i] = min(dp[i][cur_i], min( abs(cur_i - pre_i), len(ring)-abs(cur_i - pre_i) ) + dp[i-1][pre_i])
        
        res = 10**8
        for cur_i in dp[len(key)-1]:
            res = min(res, dp[len(key)-1][cur_i])
        return res + len(key)