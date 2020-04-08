class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def split(sum_):
            cur_sum, k = 0, 1
            for num in nums:
                if cur_sum + num > sum_:
                    cur_sum = num
                    k += 1
                else:
                    cur_sum += num
            return k
        
        l, r = max(nums), sum(nums)
        while l <= r:            
            mid = (l+r) // 2            
            k = split(mid)
            if k > m:
                l = mid + 1
            else:
                r = mid - 1
        return l