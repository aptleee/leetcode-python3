class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        t = 0
        while x > t:
            t = t*10 + x%10
            x //= 10

        #  two possibilities: len(x) is odd or even
        return x == t or x == t//10
