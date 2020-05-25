class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        r1 = len(S) - 1
        r2 = len(T) - 1
        while r1>=0 or r2>=0:
            c1, r1 = self.get_char(S, r1)
            c2, r2 = self.get_char(T, r2)
            # print(c1, c2, r1, r2)
            if c1 != c2:
                return False
        return True
    
    def get_char(self, S, ind):
        res = ""
        c = 0
        while ind >= 0 and not res:
            if S[ind] == "#":
                c += 1
            elif c==0:
                res = S[ind]
            else:
                c -= 1
            ind -= 1
        return res, ind