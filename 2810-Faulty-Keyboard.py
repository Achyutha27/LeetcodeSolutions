class Solution:
    def finalString(self, s: str) -> str:
        if 'i' not in s:
            return s
        ans=''
        a = s.index('i')
        while True:
            a = s.index('i')
            ans=s[a-1::-1]+s[a+1:]
            if 'i' in ans:
                a = ans.index('i')
                s = ans
                continue
            return ans