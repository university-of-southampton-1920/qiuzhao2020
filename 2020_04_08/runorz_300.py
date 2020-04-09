class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i+j)/2)
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            size = max(i+1, size)
        return size
