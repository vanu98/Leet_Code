#method-1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        result = []
        for i in nums:
            sums+=i
            result.append(sums)
        return result
       
#method-2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        for i in range(len(nums)):
            sums+=nums[i]
            nums[i]=sums
        return nums
 #method-3
 class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
