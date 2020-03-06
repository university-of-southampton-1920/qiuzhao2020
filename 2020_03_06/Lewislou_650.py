class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        d = 2
        while n > 1:
            while n%d == 0:
                count+=d
                n /= d
            d+=1
        return count
            