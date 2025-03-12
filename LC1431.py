'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
'''

'''approach
1. calculate max value in list and create a bool list of len(candies) with True values in it
2. calculate a thershold value below which any no. of candies + extra candies will remain less than max(candies)
3. iterate and update'''

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    n = len(candies)
    res = [True]*n
    i = 0
    threshold = max(candies) - extraCandies
    for i in range(n):
        if candies[i] < threshold:
            res[i] = False
    return res

#using list comprehension

def kidsWithCandies2(candies:list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]