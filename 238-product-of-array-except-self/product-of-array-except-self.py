class Solution(object):
    def productExceptSelf(self, nums):
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output.append(product)
        # return output
        
        n = len(nums)
        product_nums = [1] * n  # Initialize result array

        # Compute prefix products
        prefix = 1
        for i in range(n):
            product_nums[i] = prefix
            prefix *= nums[i]

        # Compute suffix products and multiply with prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            product_nums[i] *= suffix
            suffix *= nums[i]

        return product_nums
