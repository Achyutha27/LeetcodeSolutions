class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i]==t[i]:
                continue
            else:
                ans+= abs(i-(t.index(s[i])))
        return ans