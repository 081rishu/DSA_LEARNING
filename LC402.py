'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''

class Solution:
    def removeKdigits(self, num:str, k:int) -> str:
        if k==len(num):
            return '0'
        stack = []
        
        for ch in num:
            while stack and k and stack[-1] > ch:
                stack.pop(-1)
                k-=1
            stack.append(ch)
        
        while k:
            stack.pop(-1)
            k-=1
        res = "".join(stack).lstrip('0')

        return res if res else '0'

num = "10"
k = 1
sol = Solution()
print(sol.removeKdigits(num,k))

