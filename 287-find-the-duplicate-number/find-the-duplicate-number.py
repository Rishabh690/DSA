class Solution(object):
    def findDuplicate(self, nums):
        number = {}
        for right in range(len(nums)):
                val = nums[right]
                if val in number:
                    return val
                else:
                    number[val] = 1
        

