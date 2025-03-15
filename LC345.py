'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
'''

s = input(str)

## using a set and list
def reverseVowels(s:str) -> str:
    setOfVowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    list_of_vow = []
    res = ""
    idx = 0
    
    for i in range(len(s)):
        if s[i] in setOfVowels:
            list_of_vow.append(s[i])
    
    reversed_list = list_of_vow[::-1]
    for i in range(len(s)):
        if s[i] in setOfVowels:
            res = res+str(reversed_list[idx])
            idx+=1
        else:
            res = res+s[i]
    return res

x = reverseVowels(s)
print(x)

## using 2 pointer
def reverseVowels2(s:str) -> str:
    set_of_vowel = set("aeiouAEIOU")
    s = list(s)
    left = 0
    right = len(s)-1
    while(left<right):
        if s[left] not in set_of_vowel:
            left+=1
        elif s[right] not in set_of_vowel:
            right-=1
        else:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
    return "".join(s)

        