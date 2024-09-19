class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        prod=1
        sum=0
        for i in n:
            prod*=int(i)
            sum+=int(i)
        return prod-sum