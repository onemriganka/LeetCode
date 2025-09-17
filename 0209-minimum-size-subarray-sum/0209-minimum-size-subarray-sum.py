from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        for right in range(n):
            current_sum += nums[right]  # add the right element
            
            # shrink the window from the left as long as sum >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len

