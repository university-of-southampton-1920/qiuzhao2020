from collections import Counter
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        arr1 = [0] + arr1
        dp = [[10**8 for k in range(len(arr1))] for i in range(len(arr1))]
        dp[0][0] = -10**8
        for i in range(1, len(arr1)):
            for k in range(i+1):
                if dp[i-1][k] < arr1[i]:
                    dp[i][k] = arr1[i]
                if k > 0:
                    idx = bisect.bisect_right(arr2, dp[i-1][k-1])
                    if idx != len(arr2):
                        dp[i][k] = min(dp[i][k], arr2[idx])
        for k in range(len(arr1)):
            if dp[len(arr1)-1][k] != 10**8:
                return k
        return -1