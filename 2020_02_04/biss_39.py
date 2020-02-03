class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, 0, 0, [], res)
        return res
    
    def dfs(self, arr, target, index, tmp_res, tmp_arr, res):
        if tmp_res > target:
            return
        elif target == tmp_res:
            res.append(tmp_arr.copy())
        else:
            for i in range(index, len(arr)):
                tmp_arr.append(arr[i])
                self.dfs(arr, target, i, tmp_res+arr[i], tmp_arr, res)
                tmp_arr.pop()