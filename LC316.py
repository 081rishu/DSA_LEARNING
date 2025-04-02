'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
'''

class Solution:
    def removeDuplicates(self, s:str) -> str:
        last_occuerence = {ch:i for i, ch in enumerate(s)}
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen():
                continue

            while stack and stack[-1] > ch and last_occuerence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)