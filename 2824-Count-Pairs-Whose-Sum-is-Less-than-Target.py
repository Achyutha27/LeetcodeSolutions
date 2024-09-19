from itertools import combinations
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans=0
        for comb in combinations(nums,2):
            if sum(comb)<target:
                ans+=1
        return ans