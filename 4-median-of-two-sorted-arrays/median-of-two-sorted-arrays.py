class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3) % 2 == 0 and len(nums3) > 1:
            upper_num = len(nums3)//2
            lower_num = upper_num -1
            median = (nums3[upper_num] + nums3[lower_num]) / 2.0
            return median
        elif len(nums3) % 2 != 0 and len(nums3) > 1:
            number = len(nums3)//2
            return nums3[number]
        else:
            return nums3[0]