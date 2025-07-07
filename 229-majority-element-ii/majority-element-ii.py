class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums
        res={}
        n=(len(nums) / 3)
        result=[]
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i] = 1
        for key,value in res.items():
            if value > n:
                result.append(key)
        return result 