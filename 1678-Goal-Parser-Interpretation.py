class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        command=command.replace('()','o')
        for  i in command:
            if i=='(' or i==')':
                continue
            ans+=i
        return ans