from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack, i = [Counter()], 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(Counter())
                i+=1
            elif formula[i] == ")":
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                c = stack.pop()
                num = 1
                if j != i + 1:
                    num = int(formula[i+1:j])
                for k in c:
                    stack[-1][k] += c[k] * num
                i = j
            else:
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j+=1
                num_j = j
                while num_j < len(formula) and formula[num_j].isdigit():
                    num_j += 1
                num = 1
                if num_j != j:
                    num = int(formula[j:num_j])
                stack[-1][formula[i:j]] += num
                i = num_j
        res = []
        for k in stack[-1]:
            if stack[-1][k] != 1:
                res.append(k+str(stack[-1][k]))
            else:
                res.append(k)
        res = sorted(res)
        return "".join(res)