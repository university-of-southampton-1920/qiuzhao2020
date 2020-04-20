from collections import Counter
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        ids = 0
        c = Counter()
        for i in range(len(req_skills)):
            if req_skills[i] not in c:
                c[req_skills[i]] = (1<<ids)
                ids += 1
        new_ps = []
        for p in people:
            tmp = 0
            for r in p:
                tmp += c[r]
            new_ps.append(tmp)
        N = (1 << len(req_skills))
        dp = [[10**8, []] for i in range(N)]
        dp[0][0] = 0
        for ii in range(len(new_ps) ):
            for i in range(N):
                j = ((i^new_ps[ii])&i) 
                if dp[j][0] + 1 < dp[i][0]:
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = dp[j][1][:] + [ii]
        # print(dp[N-1])
        return dp[N-1][1]