''' 
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        val1 = []
        num = ''
        for i in version1:
            if i == '.':
                val1.append(int(num))
                num = ''
            else:
                num+=i
        val1.append(int(num))

        val2 = []
        num = ''
        for i in version2:
            if i =='.':
                val2.append(int(num))
                num = ''
            else:
                num+=i
        val2.append(int(num))

        max_len = max(len(val1), len(val2))
        val1 += [0]*(max_len - len(val1))
        val2 += [0]*(max_len - len(val2))

        for i, j in zip(val1, val2):
            if i > j:
                return 1
            elif i < j:
                return -1
            
        return 0




sol = Solution()
version1 = "1.01"
version2 = "1.001"
print(sol.compareVersion(version1, version2))