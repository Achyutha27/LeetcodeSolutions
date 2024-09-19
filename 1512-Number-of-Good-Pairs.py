class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = Counter(nums)
        c = 0
        for key,value in m.items():
            c+=(value*(value-1))//2
        return c