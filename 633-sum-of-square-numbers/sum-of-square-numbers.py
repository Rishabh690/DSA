class Solution(object):
    def judgeSquareSum(self, c):
        a, b = 0, int(math.sqrt(c))
    
        while a <= b:
            current = a * a + b * b
            if current == c:
                return True
            elif current < c:
                a += 1
            else:
                b -= 1

        return False