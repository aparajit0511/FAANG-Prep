class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        count_p = Counter(p)
        result = []

        for i in range(len(s)):
            dummy_str = []
            if len(s) - i >= len(p):
                for j in range(i,i+len(p)):
                    # print(j)
                    dummy_str.append(s[j])

                if Counter(dummy_str) == count_p:
                    result.append(i)

        return result



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        start ,end = 0 , 0
        count_p = Counter(p)
        result = []

        while end < len(s):

            if end - start + 1 == len(p):
                # print(s[start:end+1])
                if Counter(s[start:end+1]) == count_p:
                    result.append(start)
                start += 1

            end += 1

        return result