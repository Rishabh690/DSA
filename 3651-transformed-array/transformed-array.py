class Solution(object):
    def constructTransformedArray(self, nums):
        output=[]
        for i in range(len(nums)):
            move=nums[i]
            new_index = (i+move) %  len(nums)
            print(new_index)
            output.append(nums[new_index])
        return output
