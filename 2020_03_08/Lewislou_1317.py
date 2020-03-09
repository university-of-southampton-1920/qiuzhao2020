class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            A = n-i
            if '0' in str(A) or '0' in str(i):
                continue
            else:
                return [i,A]
                