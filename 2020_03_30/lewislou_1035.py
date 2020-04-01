class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m,n = len(A),len(B)
        prev,cur = [0]*(n+1),[0]*(n+1)
        for i in range(m):
            cur,prev = prev,cur
            for j in range(n):
                if A[i] == B[j]:
                    cur[j+1] = prev[j]+1
                else:
                    cur[j+1] = max(prev[j+1],cur[j])
        return cur[-1]