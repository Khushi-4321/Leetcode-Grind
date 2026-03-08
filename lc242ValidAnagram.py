# LeetCode #242 - Valid Anagram
# Accepted: 54/54 | Runtime: 19ms

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        if str1 == str2:
            return True
        else:
             return False 