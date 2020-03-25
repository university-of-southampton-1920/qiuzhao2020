class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # dummymap = set()
        # res = 0
        # n = len(A)
        # for i in range(n):
        #     dummymap.add(i)
        #     j = i
        #     for j in range(i):
        #         diff = A[i] - A[j]
        #         if diff < float('-inf') or diff > float('inf'):
        #             continue
        #         d = diff
        #         c1 = dummymap.update(d)
        #         c2 = dummymap.update(d)
        #         res += c2
        #         dummymap[d] = c1 + c2 + 1
        # return res
        # for collections import defaultdict
        total = 0
        dp = [defaultdict(int) for i in A]
        n = len(A)
        for i in range(n):
            for j in range(i):
                temp = A[i] - A[j]
                dp[i][temp] += 1
                if A[i] - A[j] in dp[j]:
                    dp[i][temp] += dp[j][temp]
                    total += dp[j][temp]

        return total