class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        num_stack = []
        num = 0
        string_stack = []
        res = ''
        for i in range(n):
            if s[i].isdigit():
                num = num*10+int(s[i])
            elif s[i] == '[':
                num_stack.append(num)
                num = 0
                string_stack.append(res)
                res = ''
            elif s[i] == ']':
                res = string_stack.pop()+res*num_stack.pop()
            else:
                res += s[i]
        return res
                