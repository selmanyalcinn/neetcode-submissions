class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stack=[]
        res=1
        resStack=[]
        nums=sorted(list(set(nums)))
        if nums==[]:
            return 0
        for elem in nums:
            if len(stack)!=0:
                if stack[-1]+1==elem:
                    res+=1
                    stack.append(elem)
                else:
                    resStack.append(res)
                    stack=[]
                    res=1
                    stack.append(elem)
            elif len(stack)==0:
                stack.append(elem)
        resStack.append(res)
        return max(resStack)    
        