class Solution(object):
    def findLucky(self, arr):
        result = -1 
        num_count = {}

        for i in arr :
            if i in num_count:
                num_count[i] +=1
            else:
                num_count[i] = 1
        print(num_count)
        for key, value in num_count.items():
            if key == value:
                result = max(result, key)
        
        return result