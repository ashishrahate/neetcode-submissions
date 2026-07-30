class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedN = sorted(nums)
        res= []
        numMap ={}
        for n in sortedN:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
        maxNums= sorted(numMap.values(), reverse=True)
        print(maxNums)
        i=0
        while i < k:
            for key in numMap.keys():
                if numMap[key] == maxNums[i] and key not in res:
                    res.append(key)
            i += 1
        return res




        