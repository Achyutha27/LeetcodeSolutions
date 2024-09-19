class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [0]
        left = 0
        res = []
        right = sum(nums)
        for i in range(len(nums)):
            right -=nums[i]
            res.append(abs(left-right))
            left+=nums[i]
        return res
