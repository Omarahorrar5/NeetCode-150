from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if map.get(sortedStr, 0) == 0:
                map[sortedStr] = []
            map[sortedStr].append(str)
        return list(map.values())

solution = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(solution.groupAnagrams(strs))