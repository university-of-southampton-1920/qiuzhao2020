class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        if k == 0:
            return [[]]
        elif k == 1:
            for i in range(1, n+1):
                result.append([i])
            return result
        
        elif k == n:
            return [[i for i in range(1, n+1)]]
        
        result = self.combine(n - 1, k - 1) #with n
        result2 = self.combine(n - 1, k)
        
        for res in result:
            res.append(n)

        
        result += result2
        
        return result