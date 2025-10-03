class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. remove leading spaces
        if not s:
            return 0
        
        # 2. handle sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # 3. read digits
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        num *= sign
        
        # 4. clamp within range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

        