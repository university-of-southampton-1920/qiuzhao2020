class Solution:
    def nthUglyNumber(self, n: int) -> int:
        t2, t3, t5 = 0,0,0
        q = [1]
        mark = dict()
        t = 1
        while len(q) != n:
            t = min( q[t2]*2, q[t3]*3, q[t5]*5 )
            if t == q[t2]*2:
                t2+=1
            elif t == q[t3]*3:
                t3+=1
            else:
                t5+=1
            if not (t in mark):
                mark[t] = 1
                q.append(t)
        return t