class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums = sorted(nums)
        res = list()
        result = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] == 1:
                result = result + 1
            else:
                res.append(result)
                result = 1
        res.append(result)
        return max(res)
