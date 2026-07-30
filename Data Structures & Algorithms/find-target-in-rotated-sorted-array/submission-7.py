class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = l + ( r- l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r] : # we are in right portion of array
                if target >  nums[mid] and target < nums[r]:
                    l  = mid + 1
                else:
                    r = mid
            else:
                if target > nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return res