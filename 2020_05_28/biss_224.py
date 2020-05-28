class Solution:
    def calculate(self, S: str) -> int:
        stack = []
        i = 0
        while i < len(S):
            if S[i] == " ":
                i += 1
                continue
            elif S[i] == ")":
                res = 0
                while stack and stack[-1] != "(":
                    num = stack.pop()
                    if stack and stack[-1] == "-":
                        res += -num
                        stack.pop()
                    else:
                        res += num
                        if stack[-1] == "+":
                            stack.pop()
                stack.pop()
                stack.append(res)
            else:
                if S[i] in {"-", "+", "("}:
                    stack.append(S[i])
                else:
                    num = ""
                    while i<len(S) and S[i].isdigit():
                        num += S[i]
                        i += 1
                    stack.append(int(num))
                    i-=1
            i += 1
        res = 0
        while stack and stack[-1] != "(":
            num = stack.pop()
            if stack and stack[-1] == "-":
                res += -num
                stack.pop()
            else:
                res += num
                if stack:
                    stack.pop()
        return res