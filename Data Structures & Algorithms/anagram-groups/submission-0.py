class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2=[sorted(list(str(x))) for x in strs]
        values = list(set(tuple(sublist) for sublist in strs2))
        myDict={}
        for elem in strs:
            if str(sorted(list(str(elem)))) in myDict.keys():
                   myDict[str(sorted(list(str(elem))))].append(str(elem))
            else:
                myDict[str(sorted(list(str(elem))))]=[str(elem)]
        return myDict.values()
        