class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        #sorted(candidates)
        candidates.sort()
        def backTrack(target, start, end, tempList):
            if target == 0:
                result.append(tempList)
                return
            
            for i in range(start, end + 1):
                if (i > start) and (candidates[i] == candidates[i-1]):
                    continue

                current = candidates[i]
                if current > target:
                    break
                    
                remain = target - current

                backTrack(remain, i+1, end, tempList + [current])
            
        backTrack(target, 0, len(candidates) - 1, [])
        
        return result