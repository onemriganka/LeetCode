class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # handle zero quickly
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                summ = mul + res[i + j + 1]
                res[i + j + 1] = summ % 10
                res[i + j] += summ // 10

        # skip leading zeros and build result
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))
        return "".join(result)

        