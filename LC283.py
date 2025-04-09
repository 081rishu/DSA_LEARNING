'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution():
    def moveZeroes(self, nums:list[int]) -> None:
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums
sol = Solution()
nums = [0,0,1]
print(sol.moveZeroes(nums))