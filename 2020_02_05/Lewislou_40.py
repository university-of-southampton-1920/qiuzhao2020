class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        list1 = [i for i in candidates if i <= target]
        def fn(nums, tmp):
            s = sum(tmp) ##sum函数点睛之笔
            if s == target:
                result.append(tmp)
            else:
                for i in range(len(nums)):
                    if s > target:
                        break
                    if i>0 and nums[i] == nums[i-1]: continue
                    fn(nums[i+1:],tmp+[nums[i]])

        s_c = sorted(list1)
        result = []
    
        fn(s_c, [])

        return result

        

##Much faster 
 class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        L, A, _ = len(candidates), [], candidates.sort()                          
        def dfs(I, P, S):
            if S == target: return A.append(P)
            for i in range(I,L):
                if i > I and candidates[i] == candidates[i - 1]: continue
                if S + candidates[i] > target: break
                dfs(i + 1, P + [candidates[i]], S + candidates[i])
        dfs(0, [], 0)
        return A       
        