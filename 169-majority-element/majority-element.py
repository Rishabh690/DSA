class Solution(object):
    def majorityElement(self, nums):
        count= 0 
        candidate = None

        for num in nums:
            if count == 0 :
                candidate = num
            count+=(1 if num == candidate else -1)
            print(count)
        return candidate
        
        
        # n=(len(nums) / 2)
        # res= {}
        # for i in nums:
        #     if i in res:
        #         res[i] +=1
        #     else:
        #         res[i] = 1
        # for key,value in res.items():
        #     if value > n:
        #         return key

