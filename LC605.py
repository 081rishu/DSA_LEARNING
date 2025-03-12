'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
'''

'''
approach:
1. calculate lenght
2. iterate over length and handle the edge plot
3. update and return'''

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    length = len(flowerbed)

    for i in range (length):
        if not flowerbed[i]:
            prev = flowerbed[i-1] if i>0 else 0
            next = flowerbed[i+1] if i<length-1 else 0

            if prev==0 and next==0:
                flowerbed[i] = 1
                n-=1

                if n==0:
                    return True
    return n<=0


flowerbed = [0,0,1,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))
