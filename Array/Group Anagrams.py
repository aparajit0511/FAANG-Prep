class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter , defaultdict

        hash_table = defaultdict()

        for word in strs:
            sorted_word = ''.join(sorted(word))
            count = Counter(word)

            if sorted_word not in hash_table:
                hash_table[sorted_word] = [word]
            else:
                hash_table[sorted_word].append(word)

        print(hash_table)
        result = []

        for keys in hash_table.keys():
            result.append(hash_table[keys])

        return result