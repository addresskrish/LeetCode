class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  
        def backtrack(pat, target, start):
            if target == 0:
                res.append(list(pat))
                return 
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                pat.append(candidates[i])
                backtrack(pat, target - candidates[i], i)
                pat.pop()

        backtrack([], target, 0)
        
        return res