import numpy as np

class Solution:
    def helper(self,dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = np.inf
            for i in range(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = self.helper(dp, mp, s)
                if (tmp != -1): 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == np.inf else ans
            return dp[target]
        
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(stickers)
        mp = [[0]*26 for _ in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
                
        return self.helper(dp, mp, target)
