class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 0 or len(A) == 1:
            return 0
        A = sorted(A)
        #dp = [0] * len(A)
        length = len(A)
        mini = 20000
        # for i in A:
        #     if i == K:
        #         result.append(i)
        for i in range(length):
            f = min(A[0] + K, A[i] - K)
            if i - 1 >= 0: 
                temp = A[i - 1] + K
            else:
                temp = A[length - 1] - K
            s = max(A[length - 1] - K, temp)
            mini = min(mini, s - f)
        return mini
                 
# class Solution:
#     def smallestRangeII(self, A: List[int], K: int) -> int:
#         # [1,3,6]
#         # [4, 1, 5 , 9] +, +
#         # [-2, ..., 9] -, + x
#         # [4, ..., 3] +, -
#         # [1, 3, 6] +, +, + | +, -, - | -, - , -
#         A = sorted(A)
#         res = A[len(A) - 1] - A[0]
#         for i in range(1, len(A)):
#             res = min(res, max(A[i-1]+K, A[len(A)-1]-K) - min(A[0]+K, A[i]-K))
#         return res