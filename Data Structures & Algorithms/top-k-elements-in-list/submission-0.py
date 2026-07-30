class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedN = sorted(nums)
        res= []
        numMap ={}
        for n in sortedN:
            if n not in res:
                if n in numMap:
                    numMap[n] += 1
                else:
                    numMap[n] = 1
                if numMap[n] >= k:
                    res.append(n)
        return res



        