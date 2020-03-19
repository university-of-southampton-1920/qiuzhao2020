class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp0 = [0 for i in range(len(arr))]
        dp1 = [0 for i in range(len(arr))]
        dp0[0] = arr[0]
        dp1[0] = arr[0]
        res = max(dp0[0], dp1[0])
        for i in range(1, len(arr)):
            dp0[i] = max(arr[i], dp0[i-1] + arr[i])
            dp1[i] = max(dp1[i-1] + arr[i], dp0[i-1], arr[i])
            res = max(res, dp0[i], dp1[i])
        return res