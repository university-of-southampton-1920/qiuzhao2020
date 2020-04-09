class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pre, curr = 0, 0
        n = len(nums)
        while curr < n:
            if nums[pre] == nums[curr]:
                curr += 1
            else:
                pre += 1
                nums[pre] = nums[curr]
                curr += 1
        return pre + 1