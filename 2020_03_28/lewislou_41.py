class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxi = len(nums)
        if maxi and max(nums)>=0:
            for i in range(1, max(nums)):
                if i not in nums: return i
            return max(nums)+1
        return 1