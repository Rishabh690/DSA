class Solution(object):
    def stringMatching(self, words):
        result=[]
        for i,j in enumerate(words) :
            for num in range(len(words)):
                if words[i] == words[num]:
                    continue
                else:
                    if words[i] in words[num] and words[i] not in result:
                        result.append(words[i])

        return result 