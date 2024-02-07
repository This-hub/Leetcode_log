class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        if n in {1,2}:
            return max(nums)
        else:

            for i in range(1,n+1):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
            return dp[n]

#用时25ms，击败99.25%
# https://leetcode.cn/problems/house-robber/submissions/501054861?envType=study-plan-v2&envId=dynamic-programming