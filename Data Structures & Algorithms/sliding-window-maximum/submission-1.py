class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        r = k-1

        curMax = max(nums[l:r+1])
        result.append(curMax)
        for r in range(k,len(nums)):
            curMax = max(curMax,nums[r])
            result.append(curMax)
        # while r<len(nums):
        #     result.append(max(nums[l:r+1]))
        #     l+=1
        #     r+=1
        return result