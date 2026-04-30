class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        cur_max = max(nums[0:k])
        result.append(cur_max)
        l = 1
        r = k
        while r<len(nums):
            cur_max = max(cur_max,nums[r])
            result.append(cur_max)
            l+=1
            r+=1
        return result