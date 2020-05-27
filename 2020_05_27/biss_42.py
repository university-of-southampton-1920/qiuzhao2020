class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                    res += w * (min(height[i], height[stack[-1]]) - base)
            stack.append(i)
        return res