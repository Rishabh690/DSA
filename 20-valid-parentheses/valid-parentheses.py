class Solution(object):
    def isValid(self, s):
        l = []
        if s[0]==")" or s[0]=="]" or s[0]=='}':
            return False
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            elif i == ')' and l and l[-1] == '(':
                l.pop()
            elif i == '}' and l and l[-1] == '{':
                l.pop()
            elif i == ']' and l and l[-1] == '[':
                l.pop()
            else:
                return False
        return not l
            
        
        # result=[]
        # poojan = {")":"(","]":"[","}":"{"}

        # for i in s:
        #     if i in poojan:
        #         if result and result[-1] == poojan[i]:
        #             result.pop()
        #         else:
        #             return False
        #     else:
        #         result.append(i)
        # return True if not result else False
        
        