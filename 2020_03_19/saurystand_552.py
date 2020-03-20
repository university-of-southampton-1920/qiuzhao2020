class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1,1,2]
        i = 2
        M = 10**9 + 7
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2]) % M)
            i += 1
        res = (nums[n] + nums[n-1] + nums[n-2]) % M
        for i in range(n):
            res += nums[i+1] * nums[n-i] % M
            res %= M
        return res