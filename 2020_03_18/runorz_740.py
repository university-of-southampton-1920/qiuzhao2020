class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev = None
        avoid, using = 0, 0
        for k in sorted(nums):
            if k == prev:
                continue
            if k-1 != prev:
                avoid, using = max(avoid, using), k*nums.count(k) + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*nums.count(k) + avoid
            prev = k
        return max(avoid, using)
