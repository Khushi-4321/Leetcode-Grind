# LC#345: Reverse Vowels - two pointer
# 480/480. Accepted

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:
            if s[left] in "aeiouAEIOU" and s[right] in "aeiouAEIOU":    
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1    
            elif s[left] not in "aeiouAEIOU":
                left+=1
            elif s[right] not in "aeiouAEIOU":
                right-= 1    
            
            
        return "".join(s)