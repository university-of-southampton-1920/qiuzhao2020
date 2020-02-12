class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # [1,3,6]
        # [4, 1, 5 , 9] +, +
        # [-2, ..., 9] -, + x
        # [4, ..., 3] +, -
        # [1, 3, 6] +, +, + | +, -, - | -, - , -
        A = sorted(A)
        res = A[len(A) - 1] - A[0]
        for i in range(1, len(A)):
            res = min(res, max(A[i-1]+K, A[len(A)-1]-K) - min(A[0]+K, A[i]-K))
        return res