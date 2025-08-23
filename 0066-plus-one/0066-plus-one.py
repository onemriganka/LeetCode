class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # if all digits are 9 (e.g., 999 -> 1000)
        return [1] + digits

        