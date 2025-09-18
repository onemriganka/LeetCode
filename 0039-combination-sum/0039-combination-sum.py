from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # if we hit the target, store the current combination
            if total == target:
                res.append(path[:])
                return
            # if we go over, no need to continue
            if total > target:
                return

            # try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])              # pick this number
                backtrack(i, path, total + candidates[i])  # stay at i (reuse allowed)
                path.pop()                              # undo the pick

        backtrack(0, [], 0)
        return res

        