class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        i=1
        a = len(nums)
        while(i!=a):
            if(nums[i-1]==nums[i]):
                del nums[i-1]
                i-=1
            i+=1
            a = len(nums)
        return len(nums)
