class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        up = 0 # should accept up
        down = 0 # should accept down 
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                down = up + 1
            elif nums[i] - nums[i-1] < 0:
                up = down + 1
        return max(down, up) + 1