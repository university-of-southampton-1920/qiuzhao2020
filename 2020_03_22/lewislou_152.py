class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = -inf
        
        for i in range(len(nums)):
            temp = 1
            for j in range(i,len(nums)):
                temp = temp*nums[j]
                if temp > maximum:
                    maximum = temp
        return maximum

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left2right = nums
        right2left = nums[::-1]
        
        for i in range(1,len(nums)):
            left2right[i] *= (left2right[i-1] or 1)
            right2left[i] *= (right2left[i-1] or 1)

        return max(max(left2right),max(right2left))