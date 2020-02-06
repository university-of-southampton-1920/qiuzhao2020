class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [i for i in itertools.combinations(range(1,n+1),k)] #迭代工具


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def cancat(nums, k, i):
            if k == 0: 
                result.append(nums)
            for j in range(i, n+1):
                cancat(nums+[j], k-1, j+1) #k-1作为选择的标准，所有递归的结果中取出长度为k的
        cancat([], k, 1)
        return result