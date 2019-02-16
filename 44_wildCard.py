class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        s_cur, p_cur, star, match= 0, 0, -1, 0
        while s_cur < len(s):
            if p_cur < len(p) and (p[p_cur] == s[s_cur] or p[p_cur] == "?"):
                p_cur += 1
                s_cur += 1
            elif p_cur < len(p) and p[p_cur] == "*":
                star = p_cur
                match = s_cur
                p_cur += 1
            else:  # no match
                if star != -1:  # there is a star
                    p_cur = star+1
                    match += 1  # match is the last char in s star matched
                    s_cur = match
                else:
                    return False
        while p_cur < len(p) and p[p_cur] == "*":
            p_cur += 1
        return p_cur == len(s)

