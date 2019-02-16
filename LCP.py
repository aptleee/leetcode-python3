class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        n = len(strs)
        if n == 0:
            return ""

        n1 = len(strs[0])
        ret = ""
        for i in range(n1):

            for j in range(1, n):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return ret


            ret += strs[0][i]

        return ret
