'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC" 
'''


'''approach:
1. let's first check that is it divisible or not
2. get the gcd of length of both strings
3. slice the substring of that length
'''
from math import gcd

# alternate fn for gcd using euclidean algo
def compute_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
        return num1


def gcdOfStrings(str1: str, str2: str) -> str:
    
    #first check for divisibility
    if str1+str2 != str2+str1:
        return ""
    
    #retreiving len of required substring
    gcd_len = gcd(len(str1), len(str2))

    #slicing the substring
    return str1[:gcd_len]

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))