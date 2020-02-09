class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = [0 for _ in range(target+1)]
        result[0] = 1
        for i in range(1,target+1):
            for e in nums:
                if e > i:
                    continue
                result[i] += result[i - e]

        return result[-1]
