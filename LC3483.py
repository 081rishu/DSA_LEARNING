'''
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.
'''

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        result = set()

        def generate_path(path, used):
            if len(path) == 3:
                if path[0] == 0:
                    return
                if path[2] % 2 != 0:
                    return
                number = path[0]*100 + path[1]*10 + path[2]
                result.add(number)
                return
            
            for i in range(len(digits)):
                if i not in used:
                    used.add(i)
                    generate_path(path + [digits[i]], used)
                    used.remove(i)
        generate_path([], set())
        return len(result)