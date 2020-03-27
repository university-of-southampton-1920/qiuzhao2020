class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pre_num = None
        for i in range(len(nums)):
            while nums[i]-1 != i and nums[i]>=1 and nums[i]<=len(nums):
                if nums[nums[i]-1] != nums[i]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    break
        # print(nums)
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i+1
        return len(nums)+1