'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for char in s:
            if char in dict:
                dict[char]+=1
            else:
                dict[char] = 1
        
        key = ""
        for keys, val in dict.items():
            if val == 1:
                key+=keys
                break
        if not key:
            return -1
        else:
            return s.index(key)
        
## lets do an optimized one
    def firstUniqChar(s:str) -> int:
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1 
        
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        return -1
    
s = "dddccdbba"
sol = Solution()
print(sol.firstUniqChar(s))