class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS,COLS = len(matrix),len(matrix[0])
        top ,bot = 0 , len(matrix)-1
        while top <= bot:
            middle = (top+bot) //2
            if target < matrix[middle][0]:
                bot= middle -1 
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break
            
        if not(top<=bot):
            return False
        middle = (top+bot)//2
        l,r = 0,COLS-1
        while l<=r:
            m=(l+r)//2
            if target < matrix[middle][m]:
                r=m-1
            elif target > matrix[middle][m]:
                l=m+1
            else:
                return True
        return False
            