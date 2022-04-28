class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sstr = ""
        r = 0
        for c in s:
            if c not in sstr:
                sstr += c
            else:
                sstr = sstr.split(c)[1] + c

            r = max(len(sstr), r)

        return r