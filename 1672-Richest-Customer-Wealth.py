class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            a = sum(i)
            if a>m:
                m=a
        return m