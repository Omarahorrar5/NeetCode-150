from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return [i,j]

solution = Solution()
nums, target = [3,4,5,6], 9
print(solution.twoSum(nums, target))