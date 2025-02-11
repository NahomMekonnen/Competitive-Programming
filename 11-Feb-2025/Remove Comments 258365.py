# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        open = False
        for line in source:
            i  = 0
            if not open:
                newLine =[]
            while i < len(line):
                if line[i:i+2] == '/*' and not open:
                    open = True
                    i += 1
                elif line[i:i+2] == '*/' and open:
                    open = False
                    i +=1
                elif not open and line[i:i+2] == '//':
                    break
                elif not open:
                    newLine.append(line[i])
                i += 1
            if newLine and not open:
                ans.append("".join(newLine))

        return ans