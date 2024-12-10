class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount = 0

        for i in range(len(s)):
            visited = set()
            for j in range(i,len(s)):
                if s[j] not in visited:
                    visited.add(s[j])
                else:
                    break

            maxCount = max(maxCount,len(visited))

        return maxCount



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount = 0
        visited = set()

        start , end = 0 , 0

        while end < len(s):

            if s[end] in visited:
                while s[end] in visited:
                    visited.remove(s[start])
                    start += 1
            
            maxCount = max(maxCount,end - start+1)
            visited.add(s[end])
            end += 1

        return maxCount 
