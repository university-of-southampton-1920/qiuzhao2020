class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        return max(self.computeMax(nums[1:]), self.computeMax(nums[:-1]))
        
    def computeMax(self, nums):
        prev_max, current_max = 0, 0
        for index, x in enumerate(nums):
                
            temp = current_max
            current_max = max(prev_max + x, current_max)
            prev_max = temp

        return current_max
        