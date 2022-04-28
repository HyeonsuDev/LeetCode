class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        val, state, idx, sign = 0, 0, 0, 1

        if len(s) == 0:
            return 0

        while idx < len(s):
            c = s[idx]

            if state == 0:
                if c == ' ':
                    state = 0
                elif c == '+' or c == '-':
                    state = 1
                    sign = 1 if c == '+' else -1
                elif c.isdigit():
                    state = 2
                    val = val * 10 + int(c)
                else:
                    return 0
            elif state == 1:
                if c.isdigit():
                    state = 2
                    val = val * 10 + int(c)
                else:
                    return 0
            elif state == 2:
                if c.isdigit():
                    state = 2
                    val = val * 10 + int(c)
                else:
                    break
            else:
                return 0

            idx += 1

        val *= sign
        val = min(val, 2**31 -1)
        val = max(-(2**32), val)

        return val



if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("0032"))