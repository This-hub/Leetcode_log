# 泰波那契序列 Tn 定义如下：
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

class Solution:
    def tribonacci(self, n: int) -> int:
        t=[0,1,1]
        if n<2:
            return t[n]
        else:

            for i in range(n-2):
                t[0],t[1],t[2]=t[1],t[2],sum(t)
            return t[2]

#用时30ms，击败94.42%