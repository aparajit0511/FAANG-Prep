class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(candidates,target,combination,result):

            if target < 0:
                return result

            if target == 0:
                result.append(combination[:])
                return result

            for i in candidates:
                combination.append(i)
                result = backtrack(candidates,target-i,combination,result)
                combination.pop()

            return result

        answer = backtrack(candidates,target,[],[])
        unique = set()

        for ans in answer:
            ans.sort()
            unique.add(tuple(ans))

        return list(unique)