class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return sum([nums[i-1]*[nums[i]] for i in range(1,len(nums),2)],[])
