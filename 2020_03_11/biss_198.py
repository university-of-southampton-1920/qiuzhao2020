class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        pp = nums[0]
        p = nums[1]
        res = max(pp, p)
        for i in range(2, len(nums)):
            tmp = pp + nums[i]
            pp = max(pp, p)
            p = tmp
            res = max(res, p, pp)
        return res