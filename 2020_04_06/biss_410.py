class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = 0, 0
        for i in range(len(nums)):
            left = max(nums[i], left)
            right += nums[i]
        while left < right:
            mid = int( (right + left) / 2) 
            print(mid, left, right)
            if self.check(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left
        
    def check(self, nums, m, val):
        c = 0
        i = 0
        while i < len(nums):
            s = 0
            j = i
            while j < len(nums):
                s += nums[j]
                if s > val:
                    break
                j+=1
            i = j
            c+=1
            if c > m:
                return False
        return True