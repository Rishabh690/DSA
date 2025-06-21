class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset=set()
        left = 0 
        max_string = 0 
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            max_string = max(max_string,right-left+1)
        return max_string
                        

# charset=set()
#         left = 0 
#         max_string = 0 
#         for right in range(len(s)):
#             while s[right] in charset:
#                 charset.remove(s[left])
#                 left+=1
#             charset.add(s[right])
#             max_string = max(max_string,right-left+1)
#         return max_string
