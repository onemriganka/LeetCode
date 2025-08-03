class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # a = ways to reach step (n-2), b = (n-1)
        for _ in range(3, n + 1):
            a, b = b, a + b  # Fibonacci logic

        return b

        