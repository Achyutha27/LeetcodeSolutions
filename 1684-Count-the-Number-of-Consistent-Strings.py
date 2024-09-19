class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed=set(allowed)
        for i in words:
            if all(char in allowed for char in i):
                ans+=1
        return ans
        