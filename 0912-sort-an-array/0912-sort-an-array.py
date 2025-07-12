# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         a = sorted(nums)
 
#         for i in range(len(a)):
#             nums[i] = a[i] 
#         return nums      
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = sorted(nums)
        return result