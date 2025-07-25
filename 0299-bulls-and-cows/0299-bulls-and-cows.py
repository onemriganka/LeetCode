class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        count_s = [0] * 10
        count_g = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                count_s[int(secret[i])] += 1
                count_g[int(guess[i])] += 1

        for i in range(10):
            cows += min(count_s[i], count_g[i])

        return f"{bulls}A{cows}B"

        