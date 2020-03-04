
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        X,N = sum(A), len(A)
        # trivial case - we can not have non empty B and C
        if N <= 1:
            return False
        # trivial case - mean(a) is an element of A - we can use B = [mean(A)]
        if X % N == 0 and (X // N) in A:
            return True
        if N == 2:
            return False
        
        mean, halfsum = X / N, X // 2
        
        # without lossing a generality C is a smaller of b and c, then its maximun length is half of N
        # there is no need to check sums of subsets longer than n // 2
        lenC = N // 2
        # dp[length of subset] = set of sums of all possible subsets of A[:i]
        DP = [set() for c in range(lenC + 1)]
        #outer loop by elements of A. use sorting to stop early. O(N)
        A = sorted(A)
        for a in A:
            #inner loop by length of subset. reverse order helps to avoid collisions. O(N)
            for c in range(lenC - 1, 0, -1):
                # we can increase every possible sum of s[i-1,c] by a new element A[i]. O(sum(A))
                for s in DP[c]:
                    #new sum will be s+a
                    sa = s+a
                    #new length of subset will be c+1
                    c1 = c+1
                    # check whether means are equal: mean(a) == mean(c), x/n == (s+a)/(c+1)
                    if X * c1 == sa * N:
                        return True
                    #shortcuts:
                    #1 no need to add big subsets to the dp
                    #2 since a is sorted, all the consequent elements will be bigger,ths mean(c) can only increase, so we can stop if (s+a)/(c+1) > mean
                    #3 no need to explore subsets if their sum is bigger than half of the sum of a
                    if c1 < lenC and sa / c1 < mean and sa < halfsum:
                        DP[c1].add(sa)
            #we can always have a subset of length 1 using only element a
            DP[1].add(a)
        return False
            
            
        
#         if len(A) == 1:
#             return False
#         sumA = 0
#         for a in A:
#             sumA += a
#         A = sorted(A)
#         alen = len(A)
#         for b in range(1, int(alen / 2) + 1):
#             if (sumA * b) % alen == 0:
#                 if self.check(A, (sumA * b) / alen, b, 0):
#                     return True
#         return False
    
#     def check(self, A, leftSum, leftNum, startIndex):
#         if leftNum == 0:
#             return leftSum == 0
#         if A[startIndex] > leftSum / leftSum:
#             return False
#         alen = len(A)
#         for i in range(startIndex, alen-leftNum+1):
#             if i > startIndex and A[i] == A[i-1]:
#                 continue
#             if self.check(A, leftSum-A[i], leftNum-1, i+1):
#                 return True
#         return False

#dalao answer
# class Solution:  # donot finish because of the 0 element corners case
#     def splitArraySameAverage(self, A: List[int]) -> bool:
#         all_sum = sum(A)
#         L = len(A)
#         dp = [[0 for i in range(all_sum+1)] for j in range(len(A)) ]
#         # initialization
#         dp[0][A[0]] = 1
        
#         # cal dp
#         for i in range(1, len(A)):
#             for v in range(1, all_sum+1):
#                 if v - A[i] >= 0:
#                     dp[i][v] = dp[i-1][v-A[i]]+1 if dp[i-1][v-A[i]] > 0 or v-A[i] == 0 else dp[i-1][v]
#                     if dp[i][v] == len(A) or dp[i][v] == 0:
#                         continue  # avoid dividing by 0 
#                     up_avg = v / dp[i][v]
#                     down_avg = (all_sum - v) / (L - dp[i][v] )
#                     if up_avg == down_avg:
#                         for k in dp:
#                             print(k)
#                         print(up_avg)
#                         print(down_avg)
#                         return True
#         for k in dp:
#             print(k)
#         return False
        