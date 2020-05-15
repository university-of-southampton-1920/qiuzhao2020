from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        q = deque()
        presum = [0 for i in range(len(A))]  # presum[0] = 0
        res = 10**8
        presum[0] = A[0]
        for i in range(1, len(A)):
            presum[i] = presum[i-1] + A[i]
        # print(presum)
        for i in range(len(presum)):
            while len(q) and presum[i] - presum[q[0]] >= K:
                res = min(res, i - q[0])
                # print(i, q[0], presum[i], presum[q[0]])
                # print(q)
                q.popleft()
            if presum[i] >= K:
                res = min(res, i+1)
            while len(q) and presum[i] <= presum[q[-1]]:
                q.pop()
            q.append(i)
        return res if res != 10**8 else -1