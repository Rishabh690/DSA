class Solution(object):
    def isPossibleToSplit(self, nums):
        n=len(nums)
        nums1=[]
        nums2= []
        if n == 0:
            return False 
        if n%2 != 0:
            return False
        first_element = nums[0]
        freq = Counter(nums)
        for count in freq.values():
            if count > 2:
                return False
        return True

        
        