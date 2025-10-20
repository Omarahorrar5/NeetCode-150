from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sortedMap = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        return list(sortedMap.keys())[:k]
    
solution = Solution()
nums = [1,2,2,3,3,3]
print(solution.topKFrequent(nums, 2))