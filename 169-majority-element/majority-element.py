class Solution(object):
    def majorityElement(self, nums):
        n=(len(nums) / 2)
        res= {}
        for i in nums:
            if i in res:
                res[i] +=1
            else:
                res[i] = 1
        for key,value in res.items():
            if value > n:
                return key

