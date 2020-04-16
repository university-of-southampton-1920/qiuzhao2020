class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        dp0 = 0
        dp1 = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp0_ = dp0
                dp1_ = dp1 + 1
                if A[i] > B[i-1] and B[i] > A[i-1]:
                    dp0_ = min(dp0_, dp1)
                    dp1_ = min(dp1_, dp0+1)
                dp1 = dp1_
                dp0 = dp0_
            else:
                # must swap
                dp0_ = dp1
                dp1_ = dp0 + 1
                dp0 = dp0_
                dp1 = dp1_
                # print("else", dp0, dp1)
        return min(dp0, dp1)