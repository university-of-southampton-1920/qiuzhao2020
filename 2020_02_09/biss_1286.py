class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        res = []
        self.dfs(characters, combinationLength, 0, [], res)
        self.res = res
        self.next_p = 0
    
    def dfs(self, arr, k, index, tmp_arr, res):
        # 216
        if len(tmp_arr) == k:
            res.append("".join(tmp_arr))
        elif index == len(arr):
            return
        else:
            tmp_arr.append(arr[index])
            self.dfs(arr, k, index+1, tmp_arr, res)
            tmp_arr.pop()
            self.dfs(arr, k, index+1, tmp_arr, res)

    def next(self) -> str:
        res = self.res[self.next_p]
        self.next_p += 1
        return res

    def hasNext(self) -> bool:
        return self.next_p < len(self.res)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()