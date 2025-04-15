'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1 = dict()
        dict2 = dict()
        res = []
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1

        for i in dict1:
            if i in dict2:
                freq = min(dict1[i], dict2[i])
                for _ in range(freq):
                    res.append(i)
        return res
    

nums1 = [1,2,2,1]
nums2 = [2,2]
sol = Solution()
print(sol.intersect(nums1, nums2))