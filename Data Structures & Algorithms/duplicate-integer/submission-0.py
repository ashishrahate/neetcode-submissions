class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        setnum = set(nums)
        res = True if len(setnum) != len(nums) else res
        return res
