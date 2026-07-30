class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) -1
        while l <= r:
            # if nums[l] < nums[r]:
            #     res = min(nums[l], res)
            #     break
            
            mid = l+ (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]

