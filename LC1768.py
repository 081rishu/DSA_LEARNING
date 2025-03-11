'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        i=0
        res = ""
        while(i<len1 and i<len2):
            res+=word1[i]
            res+=word2[i]
            i+=1
        
        if  len1>len2:
            res+=word1[i:]
        elif len2>len1:
            res+=word2[i:]
        return res
    
def mergeAlternatively(word1:str, word2:str) -> str:
    res = []
    len1 = len(word1)
    len2 = len(word2)
    i = 0
    while i<len1 and i<len2:
        res.append(word1[i])
        res.append(word2[i])
        i+=1
    res.append(word1[i:])
    res.append(word2[i:])
    return "".join(res)
    
word1 = "ab"
word2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word1, word2))