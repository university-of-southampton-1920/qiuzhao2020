class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(first, curr):
            print(id(curr))
            if len(curr) == k:
                res.append(curr[:])  # copy
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        print(id(res))
        backtrack(1, [])

        return res