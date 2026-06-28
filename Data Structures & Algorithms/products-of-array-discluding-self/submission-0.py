class Solution(object):
    def productExceptSelf(self, nums):
        right=[1]
        left=[1]
        res=[]
        prefix=1
        for i in range(0,len(nums)-1,1):
            prefix*=nums[i]
            right.append(prefix)
        print(right)
        prefix=1
        for i in range(len(nums)-1):
            prefix*=nums[-(i+1)]
            left.append(prefix)
        print(left[::-1])
        left=left[::-1]
        for i in range(len(nums)):
            rightElem=right[i]
            leftElem=left[i]
            res.append(leftElem*rightElem)
        return res


        


            
        
        

        