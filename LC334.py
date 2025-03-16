'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:
'''

def increasingTriplet(nums: list[int]) -> bool:
    small = float('inf')
    mid = float('inf')
    for num in nums:
        if num <= small:
            small = num
        elif num <= mid:
            mid = num
        else:
            return True
    
    return False


nums = input(list())
print(increasingTriplet(nums))
