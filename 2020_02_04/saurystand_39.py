class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sotred(candidates)
        #self.backTrack(result, [], candidates, target, 0, len(candidates) - 1)
       
        def backTrack(target, start, end, tempList):
            if target == 0:
                result.append(tempList)
                return
            for i in range(start, end + 1):
                if candidates[i] > target:
                    break
                remain = target - candidates[i]
                if remain and remain < candidates[0]:
                    continue
                #tempList.append(candidates[i])
                backTrack(remain, i, end, tempList + [candidates[i]])
            
        backTrack(target, 0, len(candidates) - 1, [])
        
        return result
#     def backTrack(self, result: List[int], tempList: List[int], candidates: List[int], target: int, start: int, end: int):
#         if target == 0:
#             result.append(tempList)
#             return
            
#         for i in range(start, end + 1):
#             if candidates[i] > target:
#                 break
#             remain = target - candidates[i]
#             if remain and remain < candidates[0]:
#                 continue
#             self.backTrack(result, tempList, candidates, remain, i, end)
            
            
#         # length = len(candidates)
#         # if remain == 0:
#         #     result.append(tempList)
#         # else:
#         #     for i in range(start, length):  
#         #         if not (candidates[i] > remain):
#         #             tempList.append(candidates[i])
#         #             self.backTrack(result, tempList, candidates, remain - candidates[i], i)
#         #             tempList.pop(len(tempList) - 1)
