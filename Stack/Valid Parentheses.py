class Solution:
    def isValid(self, string: str) -> bool:
        
        hash_table = {
        '(' : 0,
        ')' : 0,
        '[' : 0,
        ']' : 0,
        '{' : 0,
        '}' : 0
        }

        for s in string:
            hash_table[s] += 1

        if hash_table['('] != hash_table[')']:
            return False
        elif hash_table['['] != hash_table[']']:
            return False
        elif hash_table['{'] != hash_table['}']:
            return False

        return True



class Solution:
    def isValid(self, string: str) -> bool:

        if len(string) == 1:
            return False

        hash_table = {
        '(' : ')',
        '[' : ']' ,
        '{' : '}' 
        }

        stack = []

        for s in string:

            if stack and stack[-1] not in hash_table :
                return False
            elif stack and hash_table[stack[-1]] == s:
                stack.pop()
                continue

            stack.append(s)

        if stack:
            return False

        return True