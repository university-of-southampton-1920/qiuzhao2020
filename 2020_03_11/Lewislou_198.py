class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,current = 0,0
        for index, x in enumerate(nums):
            temp = current
            current = max(prev+x,current)
            prev = temp
        return current