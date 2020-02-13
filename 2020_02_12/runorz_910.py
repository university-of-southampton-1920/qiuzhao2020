class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        result = A[-1] - A[0]
        for i in range(len(A)-1):
            result = min(result, (max(A[-1]-K, A[i]+K) - min(A[i+1]-K, A[0]+K)))
        return result
