class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i = 0
        j = 0
        k = 0
        count = 1
        while(count < n):
            val = min(res[i]*2,res[j]*3,res[k]*5)
            if val == res[i]*2:
                i += 1
            if val == res[j]*3:
                j += 1
            if val == res[k] * 5:
                k += 1
            count += 1
            res.append(val)
        return res[-1]

                