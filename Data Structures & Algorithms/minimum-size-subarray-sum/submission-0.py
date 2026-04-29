class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = len(nums) + 1

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                l += 1
                
        return 0 if res > len(nums) else res