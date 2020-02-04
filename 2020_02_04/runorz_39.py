class Solution:
    def searching(candidates, target):
        candidates = sorted(candidates)
        result = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                return result

            count = int(target / candidates[i])
            if target % candidates[i] == 0:
                result.append([candidates[i] for _ in range(count)])

            for j in range(1,count):
                temp_result = Solution.searching(candidates[i+1 : len(candidates)], target-j*candidates[i])
                for k in range(len(temp_result)):
                    temp_result[k] = temp_result[k] + [candidates[i] for _ in range(j)]
                result = result + temp_result

        return result
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return Solution.searching(candidates, target)
