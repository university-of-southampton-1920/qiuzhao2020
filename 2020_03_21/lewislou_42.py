##暴力搜索
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        leftmax = 0
        rightmax = 0
        for i in range(len(height)):
            if len(height[:i]) > 0:
                leftmax = max(height[:i+1])
            if len(height[i:]) > 0:
                rightmax = max(height[i:])
            if (min(leftmax,rightmax)-height[i]) < 0:
                ans+=0
            else:
                ans += (min(leftmax,rightmax)-height[i])
        return ans
##Dynamic programming
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        if len(height) == 0:
            return 0
        leftmax = [height[0]]*len(height)
        rightmax = [height[-1]]*len(height)
        for i in range(1,len(height)):
            leftmax[i] = max(height[i],leftmax[i-1])
            rightmax[len(height)-i-1] = max(height[len(height)-i],rightmax[len(height)-i])
        for i in range(len(height)):
            if (min(leftmax[i],rightmax[i])-height[i]) < 0:
                ans+=0
            else:
                ans += (min(leftmax[i],rightmax[i])-height[i])
        return ans