class Solution(object):
    def differenceOfSums(self, n, m):
        # NEW APPROACH
        total_sum = n*(n+1) // 2
        k= n//m
        divisible_sum = k * m *(k+1) // 2
        return (total_sum - divisible_sum) - divisible_sum
        # OLD APPROACH
        # num1=0
        # num2=0
        # for i in range(1,n+1):
        #     if i % m == 0:
        #         num2 += i
        #     else:
        #         num1 += i 
        # return num1-num2

        