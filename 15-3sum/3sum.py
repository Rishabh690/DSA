class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i , a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            left,right = i+1 , len(nums)-1 
            while left < right:
                threesum = a + nums[left] + nums[right]
                if threesum < 0 :
                    left += 1
                elif threesum > 0 :
                    right -= 1
                else:
                    result.append([a,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return result   

    #    output=set()
    #    for i in range(len(nums)):
    #     for j in range(i,len(nums)):
    #         for k in range(j,len(nums)):
    #             if i==j or j==k or i==k :
    #                 continue
    #             if nums[i]+nums[j]+ nums[k]==0:
    #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
    #                 output.add(triplet)
    #     return [list(triplet) for triplet in output]
        