class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = [0 for _ in range(len(nums))]
        c = [0 for _ in range(len(nums))]
        max_l, max_c = 0, 0
        for i in range(len(nums)):
            l[i], c[i] = 1, 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[i] == l[j] + 1:
                        c[i] += c[j]
                    if l[i] < l[j] + 1:
                        l[i] = l[j] + 1
                        c[i] = c[j]
            if l[i] == max_l:
                max_c += c[i]
            if l[i] > max_l:
                max_l = l[i]
                max_c = c[i]
        
        return max_c
