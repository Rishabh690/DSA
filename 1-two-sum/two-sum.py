class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(len(nums)):
                if i != j and nums[j] == remaining:
                    return sorted([i, j])