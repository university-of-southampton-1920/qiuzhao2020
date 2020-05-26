class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for s in S:
            if s == "(":
                stack.append(s)
            else:  # s == ")"
                if stack[-1] == "(":
                    stack.pop()
                    tmp = 1
                    if stack and stack[-1] not in {"(", ")"}:
                        tmp += stack.pop()
                    stack.append(tmp)
                else:
                    tmp = stack.pop() * 2
                    stack.pop()
                    if stack and stack[-1] not in {"(", ")"}:
                        tmp += stack.pop()
                    stack.append(tmp)
        return stack[-1]
                