class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the list so the two-pointer technique can be used.
        result = []  # Store the valid triplets that are found.

        for i,a in enumerate(nums):
            if i>0 and a== nums[i-1]: # Skip duplicate elements to avoid repeating the same triplet.
                continue
            l, r = i+1, len(nums)-1  # Initialize two pointers.
            while l < r:
                threesum = a + nums[l] + nums[r]  # Calculate the sum of the triplet.
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -=1
                else:
                    result.append([a, nums[l], nums[r]])  # Add the valid triplet to the result.
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:  # Skip duplicates for the left pointer.
                        l += 1
                    while l < r and nums[r] == nums[r+1]:  # Skip duplicates for the right pointer.
                        r -= 1
        return result  # Return the list of unique triplets that sum to zero.