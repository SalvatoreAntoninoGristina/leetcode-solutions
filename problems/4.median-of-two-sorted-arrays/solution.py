#soluzione poco efficiente O((n + m) log(n + m))
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = sorted(nums1 + nums2)
        mid = len(merged) // 2

        if len(merged) % 2: return merged[mid]
        else: return (merged[mid - 1] + merged[mid]) / 2

        #return float(nums[mid] if length % 2 else (nums[mid-1] + nums[mid]) / 2.0)

a = Solution().findMedianSortedArrays([1,2,3], [4,5,6])
print(a)