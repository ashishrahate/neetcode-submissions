class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []
        nums.sort()
        def dfs(index, rem_sum, path):
            if rem_sum == 0:
                results.append(path[:])
                return 
            
            for i in range(index, len(nums)):
                if nums[i] > rem_sum:
                    break
                path.append(nums[i])
                dfs(i , rem_sum - nums[i], path )
                path.pop()
        dfs(0,target,[])
        return results


            
        # results = []
        # # Sort candidates to enable early pruning
        # candidates.sort()

        # def backtrack(start_index, current_target, path):
        #     if current_target == 0:
        #         results.append(path[:])
        #         return

        #     for i in range(start_index, len(candidates)):
        #         # Pruning: since candidates are sorted, if the current element exceeds 
        #         # the remaining target, all subsequent elements will too.
        #         if candidates[i] > current_target:
        #             break

        #         path.append(candidates[i])
        #         # Pass (current_target - candidate) to track remaining sum in O(1) time
        #         backtrack(i, current_target - candidates[i], path)
        #         path.pop()

        # backtrack(0, target, [])
        # return results