class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        dp = dict()
        res = 0
        for i in range(2, len(A)):
            for j in range(1, i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in s:
                    dp[(A[j], A[i])] = dp.get( ( A[i]-A[j], A[j]), 2 ) + 1
                    res = max(res, dp[(A[j], A[i])])
        return res