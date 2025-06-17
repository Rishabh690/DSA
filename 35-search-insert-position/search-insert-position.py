class Solution(object):
    def searchInsert(self, nums, target):        
        left, right = 0 , len(nums)-1
        while left<= right:
            m=(left + right) //2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m+1
            else:
                right = m-1
        return left        




        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)
