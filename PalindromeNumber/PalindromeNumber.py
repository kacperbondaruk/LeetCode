class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_input = str(x)
        reverse_number = number_input[::-1]
        if reverse_number == number_input :
            return True
        else :
            return False