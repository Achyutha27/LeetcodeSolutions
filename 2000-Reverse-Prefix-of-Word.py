class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        s = word.index(ch)
        ans = word[s::-1]+word[s+1:]
        return ans
            