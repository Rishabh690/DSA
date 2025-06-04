class Solution(object):
    def stringMatching(self, words):
        return list({w1 for i, w1 in enumerate(words)
                     for j, w2 in enumerate(words)
                     if i != j and w1 in w2})

        
        # result=[]
        # for i,j in enumerate(words) :
        #     for num in range(len(words)):
        #         if words[num] not in result:
        #             if words[i] == words[num]:
        #                 continue
        #             else:
        #                 if words[i] in words[num] and words[i] not in result:
        #                     result.append(words[i])

        # return result 