class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        n = len(s)
        if n == 0:
            return 0
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i, sum1 = n-2, table[s[-1]]
        while i >= 0:
            if table[s[i]] < table[s[i+1]]:
                sum1 -= table[s[i]]
            else:
                sum1 += table[s[i]]
            i -= 1

        return sum1
