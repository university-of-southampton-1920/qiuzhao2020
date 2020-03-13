class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = [1]
        down = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up.append(down[-1] + 1)
                down.append(down[-1])
            if nums[i] < nums[i-1]:
                down.append(up[i-1] + 1)
                up.append(up[i-1])
            if nums[i] == nums[i-1]:
                down.append(down[-1])
                up.append(up[-1])
        return max(up[-1], down[-1])
