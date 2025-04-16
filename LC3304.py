'''
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
'''

# class Solution:
#     def kthCharacter(self, k: int) -> str:
#         str = 'a'
#         aplphabets = 'abcdefghijklmnopqrstuvwxyz' 
#         for i in range(k):
#             if len(str) >= k:
#                 break
#             res = ''
#             for char in str:
#                 res += aplphabets[aplphabets.find(char) + 1
#             str += res
#         return str[k-1]


class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        def generate_str(curr_str, curr_len):
            if curr_len >= k:
                return curr_str[k-1]
            else:
                next = ''.join(alphabets[alphabets.find(char)+1] for char in curr_str)
                return generate_str(curr_str + next, len(curr_str + next))
        return generate_str('a',1)            


sol = Solution()
print(sol.kthCharacter(5))

# str = "sdlkfhsl"
# for char in str:
#     print(char)