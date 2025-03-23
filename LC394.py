'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''

class Solution:
    def decodeString(self, s:str) -> str:
        stack = []
        curr_num = ''
        curr_str = ''

        for char in s:
            if char.isdigit():
                curr_num+=char
            elif char=='[':
                stack.append((curr_str, int(curr_num)))
                curr_str = ''
                curr_num = ''
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str*num
            else:
                curr_str+=char
        return curr_str

                
sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))