class Solution:
    def isPalindrome(self, s: str) -> bool:
        inputString = ''.join(c.lower() for c in s if c.isalnum())
        
        if inputString == inputString[::-1]:
            return True
        else:
            return False