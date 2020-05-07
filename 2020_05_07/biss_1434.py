from collections import defaultdict
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        M = 10**9 + 7
        personForHat = defaultdict(list)
        for i in range(N):
            for hat in hats[i]:
                personForHat[hat].append(i)
        
        dp = [0 for i in range(1<<N)]
        dp[0] = 1
        for hat in range(1, 41):
            dp_new = dp[:]
            for state in range(1<<N):
                for p in personForHat[hat]:
                    if (state & (1<<p)):
                        continue
                    dp_new[state + (1<<p)] += dp[state]
                    dp_new[state + (1<<p)] %= M
            dp = dp_new[:]
        return dp[(1<<N)-1]