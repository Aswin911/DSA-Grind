class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        n = len(nums)

        if S % 2 != 0: return False

        target = S // 2

        dp = [[None] * (target + 1) for _ in range(n + 1)]

        def subsetSum(nums,n,target,dp):
            if target == 0: return True
            if n==0: return False

            if dp[n][target] is not None:
                return dp[n][target]

            if nums[n-1] > target:
                dp[n][target] = subsetSum(nums,n-1,target,dp)
                return dp[n][target]

            include = subsetSum(nums,n-1,target - nums[n-1],dp)
            exclude = subsetSum(nums,n-1,target,dp)
            dp[n][target] = include or exclude

            return dp[n][target]

        return subsetSum(nums,n,target,dp)







#recursion solution TLE
# def canPartition(self, nums: List[int]) -> bool:
#         S = sum(nums)
#         n = len(nums)

#         if S%2 != 0:
#             return False

#         target = S // 2

#         def subsetSum(nums,n,S):
#             if S== 0: return True
#             if n==0: return False

#             if nums[n-1] > S:
#                 return subsetSum(nums,n-1,S)

#             include = subsetSum(nums,n-1,S - nums[n-1])
#             exclude = subsetSum(nums,n-1,S)
        
#             return include or exclude
        
       
#         return subsetSum(nums,n,target)