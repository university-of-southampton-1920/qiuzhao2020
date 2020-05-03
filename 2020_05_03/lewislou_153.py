class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenth = len(nums)
        if nums[0] > nums[-1]:
            for i in range(lenth-1,0,-1):
                if nums[i] < nums[i-1]:
                    return nums[i]
        else:
            return nums[0]