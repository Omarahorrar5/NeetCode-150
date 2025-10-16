class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = {}
        
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        
        for char in t:
            if charCount.get(char, 0) == 0:
                return False
            charCount[char] -= 1
        
        return True

s = "racecar"
t = "carrace"
solution = Solution()
print(solution.isAnagram(s, t))  #True