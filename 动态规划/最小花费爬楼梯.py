# 这段代码是解决“最小花费爬楼梯”问题的一个Python解决方案。问题的大意是，给定一个整数数组cost，其中cost[i]代表达到第i个台阶所需的花费。你可以选择从第0个或第1个台阶开始爬，并且每次可以爬1个或2个台阶。
# 目标是以最小的花费达到楼梯顶部（即超过数组的最后一个元素）。这段代码使用动态规划的方法来解决这个问题。

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[0]*(n+10)
        dp[0]=0
        dp[1]=0
        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]

#38ms,击败89.97%
