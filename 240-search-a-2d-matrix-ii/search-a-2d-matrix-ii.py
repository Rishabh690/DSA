class Solution(object):
    def searchMatrix(self, matrix, target):
      col = 0 
      row_start = 0 
      row_end  = -1 
      while col <= len(matrix)-1:
        if matrix[col][row_start] <= target:
            if target in matrix[col]:
                return True 
            else:
                col +=1
        else:
            return False


