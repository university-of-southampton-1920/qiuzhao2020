class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        if len(A) == 1:
            return 0
        else:
            res = A[-1]-A[0] ##全+策略
            for i in range(len(A)-1):
                res = min(res,(max(A[i]+K,A[len(A)-1]-K) - min(A[0]+K,A[i+1]-K))) #左加右减策略
            return res