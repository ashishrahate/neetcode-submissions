class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l , r = 0 , len(nums)-1
        if l == r :
            return l 
        while l < r:
            mid = l + ( r- l) // 2

            if nums[mid] == target:
                res = mid
                return res
            elif nums[mid] > nums[r]:
                 l  = mid + 1
            else:
                r = mid
        return res