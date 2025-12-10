class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]
                result.append(new_number)
        return max(result)
 