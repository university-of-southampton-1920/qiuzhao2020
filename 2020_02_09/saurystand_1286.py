class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.result = []
        self.index = 0
        def dfs(start, path, length):
            if length == combinationLength:
                self.result.append(path)
                return
            if start == len(characters):
                return
            dfs(start + 1, path + characters[start], length + 1)
            dfs(start + 1, path, length)
        dfs(0, "", 0)
    def next(self) -> str:
        res = self.result[self.index]
        self.index += 1
        return res
    def hasNext(self) -> bool:
        return self.index != len(self.result)

#method 2     
#     def __init__(self, characters, combinationLength):
#         self.char = characters
#         self.comb = combinationLength
#         self.cur = 0
#         self.comblist = [] # ['ab','ac','bc'] # populate the list with combinationLength
#         self.helper('', 0, self.comb, self.comblist,0)
#     def helper(self, strin , ind, cap, res, cumu):
#         if cumu == cap:
#             res.append(strin)
#             return 
#         for i in range(ind, len(self.char)):
#             self.helper( strin + self.char[i] , i+1, cap,res, cumu+1 )
#     def next(self):
#         self.cur += 1
#         return self.comblist[self.cur - 1]
#     def hasNext(self):
#         return self.cur < len(self.comblist)    
    
# over time limit
#     def __init__(self, characters: str, combinationLength: int):
#         from queue import Queue
        
#         self.origin = characters
#         self.q = Queue(len(characters))
#         self.find("", 0, combinationLength)
        

#     def next(self) -> str:
#         if self.q.qsize() != 0:
#             return self.q.get()
#         return ""

#     def hasNext(self) -> bool:
#         if self.q.qsize() == 0:
#             return False
#         else:
#             return True
    
#     def find(self, string: str, index: int, length: int):
#         if length == 0: 
#             self.q.put(string)
#             return 
#         slen = len(self.origin)
#         for i in range(index, slen):
#             ch = self.origin[i]
#             self.find(string + ch, i +1, length - 1)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()