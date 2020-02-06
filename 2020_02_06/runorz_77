class Solution:
    def searching(m:int,n:int, k:int):
        if k == 1:
            return [[i] for i in range(m, n+1)]
        result = []
        for i in range(m, n+1):
            temp_result = Solution.searching(i+1, n, k-1)
            for j in range(len(temp_result)):
                temp_result[j].append(i)
                result.append(temp_result[j])
        return result
    def combine(self, n: int, k: int) -> List[List[int]]:
        return Solution.searching(1, n, k)
