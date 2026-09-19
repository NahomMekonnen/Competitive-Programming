class Solution:
    def longestWord(self, words: List[str]) -> str:
        exists = defaultdict(bool)
        for i in words :
            exists[i] = True
        words.sort(reverse = True)
        w = []
        i, n = 0, len(words) 
        while i < n :
            if exists[words[i][0]] :
                word = words[i] 
                while exists[word] :
                    word = word[:-1]
                if word == "" :
                    w.append(words[i])    
            i += 1
        if w == [] :
            return ""
        if len(w) == 1 :
            return w[0]
        w.sort(reverse = True)
        maxLen = max([len(i) for i in w ])
        longestwords = sorted([i for i in w if len(i) == maxLen ])
        return longestwords[0]

