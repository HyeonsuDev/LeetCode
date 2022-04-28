class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sstr = ""
        max = 0
        for c in s:
            if c not in sstr:
                sstr += c
            else:
                sstr = sstr.split(c)[1] + c

            if len(sstr) > max:
                max = len(sstr)

        return max

def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()