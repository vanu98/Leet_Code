class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        sum = 0
        for i in ops:
            if(i=="C"):
                pop = points.pop()
                sum-=pop
            elif (i=="D"):
                num = points[-1]*2
                sum+=num
                points.append(num)
            elif (i=="+"):
                sum+=(points[-1]+points[-2])
                points.append(points[-1]+points[-2])
            else:#elif(i.isdigit()):
                points.append(int(i))
                sum +=int(i)
        return sum
