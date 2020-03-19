class Solution:
    def checkRecord(self, n: int) -> int:
        mode = 10**9 + 7
        A = [0 for _ in range(n)]
        P = [0 for _ in range(n)]
        L = [0 for _ in range(n)]
        
        if n == 1:
            return 3
        
        if n == 2:
            return 8
        
        P[0] = 1
        L[0] = 1
        L[1] = 3
        A[0] = 1
        A[1] = 2
        A[2] = 4
        
        
        for i in range(1, n):
            A[i-1] %= mode
            P[i-1] %= mode
            L[i-1] %= mode
            
            P[i] = ((A[i - 1] + P[i - 1]) % mode + L[i - 1]) % mode
            
            if(i > 1):
                L[i] = ((A[i - 1] + P[i - 1]) % mode + (A[i - 2] + P[i - 2]) % mode) % mode
            
            if(i > 2):
                A[i] = ((A[i - 1] + A[i - 2]) % mode + A[i - 3]) % mode
                
        return ((A[n - 1] % mode + P[n - 1] % mode) % mode + L[n - 1] % mode) % mode
