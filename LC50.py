'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
'''

class Solution:
    def myPow(self, x: int, n: float) -> float:
        if n == 0:
            return 1
        if n < 1:
            return 1/ self.myPow(x, -n)
        
        half = self.myPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half
    
sol = Solution()
x = 2.00000
n = 10
print(pow(x,n))