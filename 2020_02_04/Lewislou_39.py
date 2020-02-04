class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        list1 = [i for i in candidates if i <= target]
        list1.sort()
        result = []
        answer = []
        self.compute(list1,target,0,result,answer)
        return answer
		##类似的递归方法也可以使用在深度优先搜索的回溯上
    def compute(self,list1,target,start,result,answer):
        for i in range(start,len(list1)):            
            if target > 0:
                result.append(list1[i])
                self.compute(list1,target-list1[i],i,result,answer)
                result.pop()
            elif target < 0:
                return
            else:
                temp = result[:]
                answer.append(temp)
                return


  ###NB solution          
 class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        def fn(nums, tmp):
            s = sum(tmp) ##sum函数点睛之笔
            if s == target:
                result.append(tmp)
            else:
                for i in range(len(nums)):
                    if s + nums[i] > target:
                        break
                    fn(nums[i:], tmp + [nums[i]]) ##从list第i个元素开始递归避免重复

        s_c = sorted(candidates)d
        result = []
    
        fn(s_c, [])

        return result


            
               