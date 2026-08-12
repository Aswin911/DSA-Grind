class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub , curr = nums[0],0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxsub = max(curr,maxsub)

        return maxsub