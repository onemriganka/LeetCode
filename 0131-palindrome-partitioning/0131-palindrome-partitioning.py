class Solution:
    def partition(self, s: str):
        result = []
        
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])
        
        backtrack(0, [])
        return result

        