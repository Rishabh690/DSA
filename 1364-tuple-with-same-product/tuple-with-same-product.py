class Solution(object):
    def tupleSameProduct(self, nums):
        prod_count=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                product = nums[i] * nums[j] 
                prod_count[product] += 1
        result = 0
        for count in prod_count.values():
            if count > 1:
                result += count * (count - 1) * 4  # 4 permutations per unique pair pairing
        return result
