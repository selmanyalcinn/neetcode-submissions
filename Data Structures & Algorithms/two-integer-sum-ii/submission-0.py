class Solution(object):
    def twoSum(self, numbers, target):
        l,r=0,len(numbers)-1
        while l < r:
            curSum=numbers[l]+numbers[r]
            print(curSum)
            if curSum>target:
                r=r-1
            elif curSum<target:
                l=l+1
            elif curSum==target:
                return [l+1,r+1]