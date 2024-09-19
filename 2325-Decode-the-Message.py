class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        ans={}
        answer = ''
        idx = 0
        for char in key:
            if char!=" " and char not in ans:
                ans[char]=idx
                idx+=1
        for char in message:
            if char==" ":
                answer+=' '
            else:
                answer+=s[ans[char]]
        return answer