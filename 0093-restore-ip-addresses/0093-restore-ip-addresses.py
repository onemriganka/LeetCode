class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) >= 4:
                return

            for length in range(1, 4):  # 1 to 3 digits
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res

        