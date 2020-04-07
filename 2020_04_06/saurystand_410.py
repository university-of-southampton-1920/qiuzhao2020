
#https://leetcode.com/problems/split-array-largest-sum/discuss/89819/C%2B%2B-Fast-Very-clear-explanation-Clean-Code-Solution-with-Greedy-Algorithm-and-Binary-Search
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0  # low
        right = 0  # high
        for num in nums:
            left = max(left, num)
            right += num

        while left < right:
            mid = left + int((right - left) / 2)
            if self.doable(nums, m - 1, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def doable(self, nums, cuts, maxv):
        '''
                Params:
                    nums - The input array;
                    cuts - How many cuts are available (cuts = #groups - 1);
                    max - The maximum of the (sum of elements in one group);
                Rtn:
                    Whether we can use at most 'cuts' number of cuts to segment the entire array,
                    such that the sum of each group will not exceed 'max'.
        '''
        acc = 0
        for num in nums:
            if num > maxv:
                return False
            elif acc + num <= maxv:
                acc += num
            else:
                cuts -= 1
                acc = num
                if cuts < 0:
                    return False
        return True
