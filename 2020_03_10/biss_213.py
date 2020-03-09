class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        # rob the first one
        pp = nums[0]
        p = 0
        res = nums[0]
        for i in range(2, L-1):
            tmp = pp + nums[i]
            pp = max(p, pp)
            p = tmp
            res = max(res, p, pp)
        
        # do not rob the first one
        pp = 0
        p = nums[1]
        res = max(res, pp, p)
        for i in range(2, L):
            tmp = pp + nums[i]
            pp = max(p, pp)
            p = tmp
            res = max(res, p, pp)
        return res