class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = set()
        self.dfs(candidates, target, 0, 0, [], res)
        return [list(i) for i in res]
    
    def dfs(self, arr, target, index, tmp_res, tmp_arr, res):
        if tmp_res == target:
            res.add(tuple(tmp_arr))
        elif tmp_res > target or index == len(arr):
            return 
        else:
            tmp_arr.append(arr[index])
            self.dfs(arr, target, index+1, tmp_res+arr[index], tmp_arr, res)
            
            tmp_arr.pop()
            self.dfs(arr, target, index+1, tmp_res, tmp_arr, res)