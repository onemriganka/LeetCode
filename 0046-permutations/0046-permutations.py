import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = list(list(p) for p in itertools.permutations(nums))
        return  a
 
        