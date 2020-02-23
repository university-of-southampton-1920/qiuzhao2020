import itertools
class Solution:
    def countOrders(self, n: int) -> int:
        pick = ["p"+str(i) for i in range(1,n+1)]
        de = ["d"+str(i) for i in range(1,n+1)]
        result = list(itertools.permutations(pick+de))
        number = len(result)
        for row in result:
            for i in range(1,n+1):
                if row.index("p"+str(i)) > row.index("d"+str(i)):
                    number -= 1
                    break
        return number%(10**9+7)
        
        
        