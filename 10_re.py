class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        #  the key is "#", "#" can be the first char in p, that what we should avoid
        #  if # is the second char
        #  two possibilities: first of s matches first of p; first of s doesn't match first of p
        if len(p) == 0:
            return len(s) == 0
        firstMatch = (len(s) > 0) and (p[0] == s[0]) or (p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return (firstMatch and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return firstMatch and self.isMatch(s[1:], p[1:])

class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    firstMatch = (i < len(s)) and p[j] in {s[i], "."}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = (firstMatch and dp(i+1, j)) or dp(i, j+2)
                    else:
                        ans = firstMatch and dp(i+1, j+1)

            memo[i, j] = ans


            return memo[i, j]
        return dp(0, 0)


