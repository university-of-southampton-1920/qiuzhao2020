import itertools
class Solution:
    def searching(candidates, target):
        result = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                return result
            if candidates[i] == target:
                result.append([candidates[i]])
            temp_result = Solution.searching(candidates[i+1:len(candidates)], target-candidates[i])
            for j in range(len(temp_result)):
                temp_result[j].append(candidates[i])
            result = result + temp_result

        return result
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = Solution.searching(sorted(candidates), target)
        result = sorted(result)
        result = list(result for result,_ in itertools.groupby(result))
        return result
