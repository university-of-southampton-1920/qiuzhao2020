class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums)) + [0]
        n = len(nums)
        for i in range(n):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n

#         # 1. mark numbers (num < 0) and (num > n) with a special marker number (n+1)
#         n = len(nums)
#         for i in range(n):
#             if nums[i] < 0 or nums[i] > n:
#                 nums[i] = n + 1
#         # all numbers are positive now, in range1, n+1

#         for i in range(n):
#             # make each cell appearing in the array,
#             num = abs(nums[i])
#             if num > n:
#                 continue
#             # -1 for zero index based array(so the number 1 will be at pos 0)
#             num -= 1
#             if nums[num] > 0:
#                 # prevent double
#                 nums[num] = -1 * nums[num]

#         #find the first cell which isn't negative (doesn't appear in the array)
#         for i in range(n):
#             if nums[i] >= 0:
#                 return i+1
#         #no positive numbers were found, which means the array contains all numbers 1..n
#         return n+1