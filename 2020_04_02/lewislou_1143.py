class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        prev = [0]*(n+1)
        cur = [0]*(n+1)
        for i in range(m):
            prev,cur = cur,prev
            for j in range(n):
                if text1[i] == text2[j]:
                    cur[j+1] = prev[j]+1
                else:
                    cur[j+1] = max(cur[j],prev[j+1])
        return cur[-1]
                    