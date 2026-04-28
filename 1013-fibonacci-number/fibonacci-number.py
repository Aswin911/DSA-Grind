class Solution:
    def fib(self, n: int) -> int:
        if n<=0:
            return n

        prev2,prev = 0,1
        res = 0
        for i in range(2,n+1):
            res = prev2 + prev
            prev2 = prev
            prev = res

        return prev