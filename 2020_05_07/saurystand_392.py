class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hashset = {}
        for i, word in enumerate(t):
            if word not in hashset:
                hashset[word] = [i]
            else:
                hashset[word].append(i)
        print(hashset)
        target = -1
        for word in s:
            if word not in hashset: return False
            indexs = hashset[word]
            left = 0
            right = len(indexs)
            print(right)
            while left < right:
                mid = left + (right - left) // 2
                if indexs[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            if left == len(indexs):
                return False
            target = indexs[left]
        return True
