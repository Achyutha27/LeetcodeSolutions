class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        m = 0
        for g in gain:
            ans+=g
            m=max(ans,m)
        return m