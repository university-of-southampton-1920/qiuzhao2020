class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon[0])
        result = [2**31] * (n-1) + [1]
        for row in dungeon[::-1]:
            for j in range(n)[::-1]: ##逆序排列
                result[j] = max(min(result[j:j+2])-row[j],1) 
        return result[0]