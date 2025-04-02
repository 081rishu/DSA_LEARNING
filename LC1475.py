'''
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 

Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
'''

class Solution:
    def finalPrices(self, prices:list[int]) -> list[int]:
        if len(prices)==1:
            return prices
        
        n = len(prices)
        answer = []
        for i in range(n-1):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    answer.append(prices[i] - prices[j])
                    break
            else:
                answer.append(prices[i])
    
        answer.append(prices[-1])
        return answer

prices = [10,1,1,6]
# sol = Solution()
# print(sol.finalPrices(prices))
## the above solution is not what we are looking for so let's try using monotonic stack
## how do i know monotonic stack will work here, actually i dont, i am preparing monotonic stack so lets check it out

def finalPrices(prices:list[int]) -> list[int]:
    n = len(prices)
    answer = prices[:]
    stack = []

    for i in range(n):
        while stack and prices[i]<=prices[stack[-1]]:
            j = stack.pop(-1)
            answer[j] -= prices[i]
        stack.append(i)
    return answer

print(finalPrices(prices))
