class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(1, n):
            current, count, temp = result[0], 0, ""
            for ch in result:
                if ch == current:
                    count += 1
                else:
                    temp += str(count) + current
                    current, count = ch, 1
            temp += str(count) + current
            result = temp
        return result
