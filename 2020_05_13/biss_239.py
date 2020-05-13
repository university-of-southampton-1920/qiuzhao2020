from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            # drop the out-of-date data
            while len(q) and i-q[0]>=k:
                q.popleft()
            # append for the strictly-increasing arr
            while len(q) and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
            if len(q) and i >= k-1:
                res.append(nums[q[0]])
        return res