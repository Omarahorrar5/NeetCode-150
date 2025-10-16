from typing import List

class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool: #complexity: O(n^2)
        n = len(nums)
        for i in range(n):
            for k in range(i+1,n):
                if nums[k]==nums[i]:
                    return True
        return False

    def hasDuplicate2(self, nums: List[int]) -> bool: #complexity: O(n)
        return len(nums) != len(set(nums)) #set(nums) converts nums to a set, that removes duplicates
    
nums = [1,2,3,4,5,5]
s = Solution()
print(s.hasDuplicate1(nums)) #True
print(s.hasDuplicate2(nums)) #True
