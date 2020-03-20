class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        cur = arr[0]
        mw = arr[0]
        mwd = None
        for i in range(1, len(arr)):
            if mwd == None:
                if arr[i] < 0:
                    mwd = mw
            else:
                if arr[i] < 0:
                    mwd = max(mwd+arr[i], mw)
                else:
                    mwd = mwd + arr[i]
            mw = max(arr[i], arr[i] + mw)
            if mwd == None:
                cur = max(cur, mw)
            else:
                cur = max(cur, mw, mwd)
        return cur
