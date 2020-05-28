class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped: return True
        stack = []
        for num in pushed:
            stack.append(num)
            if not popped:
                break
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack
            