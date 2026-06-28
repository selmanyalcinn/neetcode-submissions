class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for elem in nums:
            if nums.count(elem)==1:
                return elem
        return -1
        