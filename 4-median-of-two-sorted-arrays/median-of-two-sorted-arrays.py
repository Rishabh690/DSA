import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1+nums2)
        n=len(nums3)
        if n % 2 != 0 :
            position = n//2
            return float(nums3[position])
        else:
            mid1 = n // 2 - 1
            mid2 = n // 2
            avg = (nums3[mid1] + nums3[mid2]) / 2.0
            return avg



