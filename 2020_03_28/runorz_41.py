class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = [False for _ in range(len(nums)+1)]
        for e in nums:
            if e > 0 and e <= len(nums):
                s[e] = True
        for i in range(1,len(nums)+1):
            if s[i] == False:
                return i
        return len(nums)+1
