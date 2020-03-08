class Solution:
    def knightDialer(self, N: int) -> int:
        d = {1:[6,8], 2:[7,9], 3:[4,8],0:[4,6],7:[2,6],
            9:[4,2],8:[1,3],4:[3,9,0],6:[1,7,0]}
        tmp = [1 for i in range(10)]
        mod = 10**9 + 7
        if N == 1:
            return 10
        for i in range(2, N+1):
            new_tmp = [0 for i in range(10)]
            for j in range(10):
                if j == 5:
                    continue
                for k in d[j]:
                    new_tmp[k] += tmp[j]
                    new_tmp[k] %= mod
            tmp = new_tmp
        return sum(tmp) % mod