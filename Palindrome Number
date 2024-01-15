class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev_n = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            rev_n = rev_n * 10 + digit
            temp //= 10
        return rev_n == x
