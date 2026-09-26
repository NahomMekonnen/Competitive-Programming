class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k = defaultdict(str)
        for i in knowledge :
            k[i[0]] = i[1]
        ans = ""
        i = 0
        while i < len(s) :
            if s[i] == "(" :
                j = i + 1
                while j < len(s) and s[j] != ")" :
                    j += 1
                if k[s[i + 1:j]] != "" :
                    ans += k[s[i + 1:j]]
                else :
                    ans += "?"
                i = j + 1
            else :
                ans += s[i] 
                i += 1
        return ans