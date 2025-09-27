class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        i = 0
        while pow(3, i) <= n:
            if pow(3, i) == n:
                return True
            i += 1
        
        return False

 
        