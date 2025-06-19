class Solution(object):
    # def minSubArrayLen(self, target, nums):
    #     left = 0 
    #     length = 0 
    #     current_sum = 0 
    #     for right in range(len(nums)):
    #         current_sum+=nums[right]
    #         while current_sum>=target:
    #             lenght = min(length,right-left+1)
    #             current_sum -= nums[left]
    #             left += 1
    #     return length if length !=float('inf') else 0

    def minSubArrayLen(self,target, nums):
            n = len(nums)
            left = 0
            current_sum = 0
            min_len = float('inf')

            for right in range(n):
                current_sum += nums[right]

                while current_sum >= target:
                    min_len = min(min_len, right - left + 1)
                    current_sum -= nums[left]
                    left += 1

            return min_len if min_len != float('inf') else 0
