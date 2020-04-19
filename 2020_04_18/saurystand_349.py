class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        res = set()
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res  # nlogn no good