class Solution:
    def isValid(self, mid, nums, m):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > m:
                    return False
        return True
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        while(left <= right):
            mid = round((left + right) / 2)
            if(self.isValid(mid, nums, m)):
                right = mid - 1
            else:
                left = mid + 1
        print(left,right)
        return round(left)
