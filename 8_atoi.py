
class Solution:
    def myAtoi(self, s: 'str') -> 'int':
        if not str or len(str) == 0:
            return 0

        i = 0
        while str[i] == " ":
            i += 1
        if i == len(str):
            return 0
        sign = 1
        if str[i] == "-" or str[i] == "+":
            sign = 1 if str[i] == "+" else -1
            i += 1
        ret = 0
        while i < len(str) and "0" <= str[i] <= "9":
            ret = ret*10 + (ord(str[i])-ord("0"))
            i += 1

        ret = sign * ret
        if ret > (1 << 31)-1:
            return (1 << 31)-1
        if ret < -(1 << 31):
            return -(1 << 31)
        return ret



