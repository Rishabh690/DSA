class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
        # for i in range(len(nums)):
        #     for j in range(i+1 ,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <=k:
        #             return True
        # return False