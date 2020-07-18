class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m=[]
        l=[]
        for i in range(n):
            m.append(nums.pop())
        m.reverse()
        count1=0
        count2 = 0
        for i in range(n*2):
            if(i%2==0):
                l.append(nums[count1])
                count1 +=1
            else:
                l.append(m[count2])
                count2 +=1
        return l
