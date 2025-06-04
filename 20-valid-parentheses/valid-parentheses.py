class Solution(object):
    def isValid(self, s):
        result=[]
        poojan = {")":"(","]":"[","}":"{"}

        for i in s:
            if i in poojan:
                if result and result[-1] == poojan[i]:
                    result.pop()
                else:
                    return False
            else:
                result.append(i)
        return True if not result else False
        
        