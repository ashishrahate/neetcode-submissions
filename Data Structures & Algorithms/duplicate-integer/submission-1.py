class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # res = False
        # setnum = set(nums)
        # res = True if len(setnum) != len(nums) else res
        # return res
        dictNum ={}
        for i in nums: 
            if i in dictNum :
                return True
            else:
                dictNum[i] = True

        return False