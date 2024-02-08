class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = [0] * 10010
        n = len(nums)
        m = 0
        for x in nums:
            cnts[x] += 1
            m = max(m, x)
        # f[i][0] 代表「不选」数值 i；f[i][1] 代表「选择」数值 i
        f = [[0] * 2 for _ in range(m+1)]
        for i in range(1, m+1):
            f[i][1] = f[i-1][0] + i * cnts[i]
            f[i][0] = max(f[i-1][1], f[i-1][0])
        return max(f[m][0], f[m][1])

#用时44ms,击败87.08%
# https://leetcode.cn/problems/delete-and-earn/submissions/501235141?envType=study-plan-v2&envId=dynamic-programming