class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right = 0, 0
        sum = nums[0]
        ans = float('inf')
        
        while right < len(nums):
            if sum < target:
                right += 1
                if right < len(nums):
                    sum += nums[right]
            else:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        
        if ans == float('inf'):
            return 0
        return ans