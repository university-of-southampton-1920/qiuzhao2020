class Solution:
    def reverseParentheses(self, S: str) -> str:
        stack = []
        for s in S:
            if s != ")":
                stack.append(s)
            else:
                tmp = []
                while stack[-1] != "(":
                    tmp.append(stack.pop())
                stack.pop()
                for t in tmp:
                    stack.append(t)
        return "".join(stack)