class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0 , len(nums)-1
        while left < right:
            middle = (left + right) //2

            if nums[middle] > nums[middle + 1]:
                right  = middle
            else:
                left = middle+1
        return left
