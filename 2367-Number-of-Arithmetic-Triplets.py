from itertools import combinations
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for comb in combinations(nums,3):
            if abs(comb[0]-comb[1])==diff and abs(comb[1]-comb[2])==diff:
                ans+=1
        return ans