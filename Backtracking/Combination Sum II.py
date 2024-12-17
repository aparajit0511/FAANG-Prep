class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        result = self.findCombinations(candidates,result,target,[])

        return result

    def findCombinations(self,candidates,result,target,combination):

        if target < 0:
            return result

        if target == 0:
            result.append(combination[:])
            return result

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            combination.append(candidates[i])
            result = self.findCombinations(candidates[i+1:],result,target-candidates[i],combination)
            combination.pop()

        return result