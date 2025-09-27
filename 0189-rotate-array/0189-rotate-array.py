class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        firstk = nums[:-k]
        lastk = nums[-k:]
        nums[:] = lastk + firstk
        return nums

 



          
        """
        Do not return anything, modify nums in-place instead.
        """
        