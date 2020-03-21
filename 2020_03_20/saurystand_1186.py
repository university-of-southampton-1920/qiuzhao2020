class Solution:
    '''
    https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377397/Intuitive-Java-Solution-With-Explanation
    '''
    def maximumSum(self, arr: List[int]) -> int:
        # if max(arr) < 0:
        # 	return max(arr)
        # if min(arr) > 0:
        # 	return sum(arr)
        n = len(arr)
        maxendhere = [0] * n
        maxstarthere = [0] * n
        maxvalue = arr[0]
        for i in range(n):
            maxendhere[i] = max(arr[i], maxendhere[i - 1] + arr[i])
            maxvalue = max(maxvalue, maxendhere[i])
        maxstarthere[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            maxstarthere[i] = max(arr[i], maxstarthere[i + 1] + arr[i])
        for i in range(1, n - 1):
            maxvalue = max(maxvalue, maxendhere[i - 1] + maxstarthere[i + 1])

        return maxvalue
