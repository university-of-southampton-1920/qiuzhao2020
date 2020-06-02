class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        if len(num) < 2: return len(num)
        a = b = 1
        for i in range(2,len(num)+1):
            if int(num[i-2:i]) >= 10 and int(num[i-2:i]) < 26:
                a,b = b,a + b
            else:
                a,b = b,b
        return b