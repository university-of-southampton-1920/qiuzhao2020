class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res
        
    def dfs(self, n, k, tmp, tmp_arr, res):
        if len(tmp_arr) == k:
            res.append(tmp_arr.copy())
        elif tmp > n:
            return 
        else:
            tmp_arr.append(tmp) # ADD
            self.dfs(n, k, tmp+1, tmp_arr, res)
            tmp_arr.pop() # DONOT ADD
            self.dfs(n, k, tmp+1, tmp_arr, res)