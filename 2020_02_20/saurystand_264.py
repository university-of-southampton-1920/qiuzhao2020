
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        index2, index3, index5 = 0,0,0
        factor2, factor3, factor5 = 2,3,5
        for i in range(1,n):
            minx = min(min(factor2, factor3), factor5)
            ugly[i] = minx
            if factor2 == minx:
                index2 += 1
                factor2 = 2 * ugly[index2]
                
            if factor3 == minx:
                index3 += 1
                factor3 = 3 * ugly[index3]
                
            if factor5 == minx:
                index5 += 1
                factor5 = 5 * ugly[index5]
                
        return ugly[n-1]

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         t2, t3, t5 = 0,0,0
#         q = [1]
#         mark = dict()
#         t = 1
#         while len(q) != n:
#             t = min( q[t2]*2, q[t3]*3, q[t5]*5 )
#             if t == q[t2]*2:
#                 t2+=1
#             elif t == q[t3]*3:
#                 t3+=1
#             else:
#                 t5+=1
#             if not (t in mark):
#                 mark[t] = 1
#                 q.append(t)
#         return t