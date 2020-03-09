class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return [[a, n-a] for a in range(n) if not '0' in f'{a}{n-a}'][0]
