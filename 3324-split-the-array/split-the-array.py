class Solution(object):
    def isPossibleToSplit(self, nums):
       
        freq = Counter(nums)
        for count in freq.values():
            if count > 2:
                return False
        return True

        
        