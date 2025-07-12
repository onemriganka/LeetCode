class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        l = 0
        r = 1
        arr= []
        while r < len(nums):
            arr.append(nums[r] - nums[l])
            l +=1
            r +=1
        return max(arr)


        
        