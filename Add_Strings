def stringtoint(num):
    result = 0
    for i in num:
        result *= 10
        for d in '0123456789':
            result += i > d
    return result
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = stringtoint(num1)
        num2 = stringtoint(num2)
        return str(num1+num2)
