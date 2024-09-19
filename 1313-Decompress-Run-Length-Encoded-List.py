class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(0,n,2):
            freq = nums[i]
            val = nums[i+1]
            while freq:
                res.append(val)
                freq-=1
        return res