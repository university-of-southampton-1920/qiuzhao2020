class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxr = nums[0]
        minr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxr, minr = minr, maxr
            
            maxr = max(nums[i]*maxr, nums[i])
            minr = min(nums[i]*minr, nums[i])
            
            res = max(maxr, res)
        return res
