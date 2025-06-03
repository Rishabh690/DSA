class Solution(object):
    def isValid(self, s):
        result = []
        closeToOpen = {")":"(","]":"[","}":"{"}

        for i in s :
            if i in closeToOpen: 
                if result and result[-1] ==closeToOpen[i]:
                    result.pop()
                else:
                    return False
            else:
                result.append(i)
        return True if not result else False