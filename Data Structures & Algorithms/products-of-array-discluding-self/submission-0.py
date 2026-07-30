class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1, prod2 = [], []
        currPrd1, currPrd2 = 1, 1
        numlen = len(nums)
        res = []
        for i in range(numlen):
            currPrd1 = currPrd1 * nums[i]
            prod1.append(currPrd1)
            currPrd2 = currPrd2 * nums[numlen-1-i]
            prod2.append(currPrd2)
        j =0
        revProd2 = list(reversed(prod2))
        while j < numlen:
            prod = 1
            if j-1 >= 0:
                prod = prod * prod1[j-1]
            if j+1 < numlen:
                prod = prod * revProd2[j+1]
            j += 1
            res.append(prod)
        return res

