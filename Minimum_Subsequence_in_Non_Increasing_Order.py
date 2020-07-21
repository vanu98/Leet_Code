class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        while sum(result)<=sum(nums):
            result.append(nums.pop())
        return result
