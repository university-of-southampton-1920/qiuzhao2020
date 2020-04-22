class Solution:
    def cost(self, s1, s2):
        i, j = 0, 0
        while i < len(s1):
            if s1[i] == s2[j]:
                j+=1
            else:
                j = 0
            i+=1
        return len(s2) - j
    
    def shortestSuperstring(self, A: List[str]) -> str:
        g = [[0 for i in range(len(A))] for j in range(len(A))]
        INT_MAX = 10**8
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                g[i][j] = self.cost(A[i], A[j])
                g[j][i] = self.cost(A[j], A[i])
        dp = [[INT_MAX for j in range(len(A))] for i in range(1<<len(A))]
        pren = [[0 for j in range(len(A))] for i in range(1<<len(A))]
        for cur in range(len(A)):
            dp[2**cur][cur] = len(A[cur])

        for s in range(1<<len(A)):
            for cur in range(len(A)):
                if ((s>>cur)&1) != 1:
                    continue
                for pre in range(len(A)):
                    if ((s>>pre)&1) != 1 or pre == cur:
                        continue
                    if dp[s][cur] > dp[s-(1<<cur)][pre] + g[pre][cur]:
                        dp[s][cur] = dp[s-(1<<cur)][pre] + g[pre][cur]
                        pren[s][cur] = pre
        # backtrack
        s = (1<<len(A)) - 1
        best_node = -1
        best_val = INT_MAX
        for i in range(len(A)):
            if dp[s][i] < best_val:
                best_val = dp[s][i]
                best_node = i
        res = A[best_node]
        cur_node = best_node
        pre_node = pren[s][cur_node]
        s -= (1<<best_node)
        while s != 0:
            cover_l = len(A[cur_node]) - g[pre_node][cur_node]
            res = A[pre_node][:len(A[pre_node])-cover_l] + res
            cur_node = pre_node
            pre_node = pren[s][cur_node]
            s -= (1<<cur_node)
            
            
        return res
                