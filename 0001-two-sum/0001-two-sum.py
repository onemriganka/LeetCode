class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputarr = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    outputarr.append(i)
                    outputarr.append(j)
                    return outputarr


 

                

 
 