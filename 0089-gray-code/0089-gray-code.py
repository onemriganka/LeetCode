class Solution:
    def grayCode(self, n: int):
        result = [0]
        for i in range(n):
            # Reflect the current sequence
            for num in reversed(result):
                result.append(num | (1 << i))
        return result
