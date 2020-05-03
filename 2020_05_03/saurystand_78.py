class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def helper(k, temp):
            res.append(temp)
            for i in range(k, n):
                helper(i+1, temp + [nums[i]])
        helper(0, [])
        return res