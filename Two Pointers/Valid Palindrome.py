import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ["".join(char for char in word if char not in string.punctuation) for word in s.split()]
        s = ''.join(s).lower()
        # print(s)

        left , right = 0 , len(s)-1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True