class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            # Find middle element
            mid = left + (right - left) // 2

            # If mid element is greater than right element,
            # minimum must be on the right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # Otherwise minimum is at mid or on the left side
            else:
                right = mid

        # left == right and points to the minimum element
        return nums[left]