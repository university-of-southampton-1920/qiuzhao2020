class Solution:
    def robbing(self, nums, s, e):
        pre = 0
        cur = 0
        for i in range(s, e+1):
            temp = max(pre+nums[i], cur)
            pre = cur
            cur = temp
        return cur
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0] if n > 0 else 0
        return max(self.robbing(nums, 0, n-2), self.robbing(nums,1,n-1))
