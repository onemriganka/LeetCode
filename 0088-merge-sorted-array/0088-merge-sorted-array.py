class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = nums1[:m] + nums2[:n]
        for i in range (len(merged)):
            nums1[i] = merged[i]
        return nums1.sort()

 