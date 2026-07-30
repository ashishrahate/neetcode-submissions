class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted(nums)
        l, r = 0, len(nums)-1
        while l < r:
            sumnum = snums[l] + snums[r] 
            if sumnum > target :
                r-= 1
            elif sumnum < target:
                l += 1
            else:
                return [l, r]
        


        