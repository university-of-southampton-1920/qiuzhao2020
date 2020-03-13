class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        for i in range(len(nums)):
            temp = max(pre+nums[i], cur)
            pre = cur
            cur = temp
        return cur
