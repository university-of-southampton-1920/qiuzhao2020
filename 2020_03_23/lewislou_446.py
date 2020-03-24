class Solution:
    def numberOfArithmeticSlices(self, A):  
        memo = collections.defaultdict(int)
        ans = 0
        for i in range(1,len(A)): 
            for j in range(i):
                d = A[i]-A[j]
                memo[(i,d)]+=memo[(j,d)]+1
                ans+=memo[(j,d)]
        return ans