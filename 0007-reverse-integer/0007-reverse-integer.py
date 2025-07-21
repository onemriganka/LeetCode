class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = int(str(x_abs)[::-1])
        
        result = sign * reversed_num
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
