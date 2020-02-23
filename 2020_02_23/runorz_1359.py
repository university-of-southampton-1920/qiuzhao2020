  class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
    def factorial(self, i):
        if i == 1:
            return 1
        return i*self.factorial(i-1)
    
    def countOrders(self, n):
        return (self.factorial(2*n) >> n) % self.mod
