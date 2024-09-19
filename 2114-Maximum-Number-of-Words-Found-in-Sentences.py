class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=[]
        for i in sentences:
            ans.append(len(i.split()))
        return max(ans)