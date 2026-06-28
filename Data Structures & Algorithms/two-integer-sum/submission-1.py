class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums)):
            for j in range(k+1,len(nums)):
                if nums[k]+nums[j]==target:
                    return [k,j]
                j+=1
            k+=1

            
        