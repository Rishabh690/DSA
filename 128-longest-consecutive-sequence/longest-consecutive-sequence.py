class Solution(object):
    def longestConsecutive(self, nums):
        # numsset=set(nums)
        # longest =0 

        # for n in nums:
        #     if (n-1) not in numsset:
        #         length = 0 
        #         while (n+ length) in numsset:
        #             length += 1
        #         longest = max(length , longest)
        # return longest
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res