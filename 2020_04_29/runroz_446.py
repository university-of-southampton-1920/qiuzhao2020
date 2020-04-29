class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [dict() for _ in range(len(A))]
        res = 0
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                c1 = dp[i].get(d, 0)
                c2 = dp[j].get(d, 0)
                res += c2
                dp[i][d] = c1 + c2 + 1
        return res
