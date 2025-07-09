class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0    #left and right are index 
        right = n-1
        max_area = 0

        while left < right:
            w = right - left
            h = min(height[left],height[right])
            area = w*h
            max_area = max(max_area,area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area
        
        #time complexity = o(n)
        