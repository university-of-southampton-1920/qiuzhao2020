class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        '''
        For each A[i] find previous 2 elements sum up to A[i],
        then it's a classical follow up problem for Two Sum
        167. Two Sum II - Input array is sorted
        if 2 elements A[l] and A[r] sum up to A[i]
        dp[r][i]: length of longest fibonacchi sequence end with A[r], A[i]
        dp[r][i] = dp[l][r] + 1
        return the max(all posible dp[r][i])
        n**2, n**2
        '''
        n = len(A)
        max_res = 0
        dp = [[0 for i in range(n)] for j in range(n) ]
        for i in range(1,n):
            l = 0
            r = i-1
            while l < r:
                sumA = A[l] + A[r]
                if sumA > A[i]:
                    r -= 1
                elif sumA < A[i]:
                    l += 1
                else:
                    dp[r][i] = dp[l][r] + 1
                    max_res = max(max_res, dp[r][i])
                    r -= 1
                    l += 1
        if max_res == 0:
            return max_res
        else:
            max_res += 2
        return max_res


# class Solution:
#     def lenLongestFibSubseq(self, A: List[int]) -> int:
#         s = set(A)
#         dp = dict()
#         res = 0
#         for i in range(2, len(A)):
#             for j in range(1, i):
#                 if A[i] - A[j] < A[j] and A[i] - A[j] in s:
#                     dp[(A[j], A[i])] = dp.get( ( A[i]-A[j], A[j]), 2 ) + 1
#                     res = max(res, dp[(A[j], A[i])])
#         return res