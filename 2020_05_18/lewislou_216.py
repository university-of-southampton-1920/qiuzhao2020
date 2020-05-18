class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtracking(first,curr,val):
            if len(curr)==k and val==n:
                result.append(curr)
                return
            elif val<n and len(curr)<k:
                for i in range(first,10):
                    backtracking(i+1,curr+[i],val+i)
        backtracking(1,[],0)
        return result