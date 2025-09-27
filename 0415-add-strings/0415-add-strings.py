class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = []

        # pad the shorter string with zeros on the left
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        # go through each digit from right to left
        for i in range(max_len-1, -1, -1):
            n1 = int(num1[i])
            n2 = int(num2[i])
            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])

 
 
        