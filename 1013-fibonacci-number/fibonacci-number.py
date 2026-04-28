class Solution:
    def fib(self, n: int) -> int:
        if n<=0:
            return n

        prev2,prev = 0,1

        for i in range(2,n+1):
            temp = prev
            prev = prev + prev2
            prev2 = temp

        return prev