class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        j=-1
        for i in range(1,n):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                newn = target -nums[i]
                j = temp.index(newn)
                break
        if j>=0:
            return [j,i]
