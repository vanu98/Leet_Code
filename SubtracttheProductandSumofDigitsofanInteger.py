class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        a = [int(i) for i in list(str(n))]
        for i in a: mul*=i
        return mul - sum(a)
            
