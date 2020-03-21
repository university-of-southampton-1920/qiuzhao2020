class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_pos = 0
        max_neg = 0
        res = -10**8
        for i in range(len(nums)):
            if nums[i] < 0:
                max_pos_ = max(nums[i], max_neg*nums[i])
                max_neg = min(nums[i], max_pos*nums[i])
                max_pos = max_pos_
            else:
                max_pos = max(nums[i], max_pos*nums[i])
                max_neg = min(nums[i], max_neg*nums[i])
            res = max(res, max_pos)
        return res