class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        max_l, max_r = height[0], height[len(height)-1]
        A = height
        l, r = 0, len(A)-1
        res = 0
        while l <= r:
            if A[l] < A[r]:
                max_l = max(max_l, A[l])
                res += max_l - A[l]
                # print("l", res, l)
                l+=1
            else:
                max_r = max(max_r, A[r])
                res += max_r - A[r]
                # print("r", res, r)
                r-=1
        return res