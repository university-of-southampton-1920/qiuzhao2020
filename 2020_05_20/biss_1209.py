class Solution:
    def removeDuplicates(self, S: str, k: int) -> str:
        stack = []
        for s in S:
            if len(stack) == 0:
                stack.append((s, 1))
            else:
                if stack[-1][0] == s:
                    if stack[-1][1] + 1 == k:
                        for i in range(k-1):
                            stack.pop()
                    else:
                        stack.append((s, stack[-1][1]+1))
                else:
                    stack.append((s, 1))
        res = ""
        for s in stack:
            res += s[0]
        return res
                    