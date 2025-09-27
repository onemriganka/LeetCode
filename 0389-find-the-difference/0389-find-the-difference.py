class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = list(s)
        s2 = list(t)
        s1.sort()
        s2.sort()
        result = s2[:]
        for x in s1:
            if x in s2:
                result.remove(x)
 
   
        return "".join(result)

        