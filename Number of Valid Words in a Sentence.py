class Solution:
    def countValidWords(self, sentence: str) -> int:
        def checker(self, word: str) -> bool :
            has_digits = any(i.isdigit() for  i in word)
            if has_digits :
                return False
            for i in range(len(word)) :
                if word[i] == "-" :
                    if word.count('-') > 1 :
                        return False
                    if i == 0 or i == len(word) - 1 :
                        return False
                    if not word[i - 1].isalpha() or not word[i + 1].isalpha() :
                        return False

            special_chars = ['!', '.', ',']
            has_special_chars = any(i in special_chars for i in word)
            if has_special_chars :
                cnt, char = 0, ''
                for i in word :
                    if i in special_chars :
                        cnt += 1
                        char = i 
                    if cnt > 1 :
                        return False
                pos, end = word.index(char), len(word) - 1
                if pos != end : 
                    return False
            return True
        return len([i for i in sentence.split() if checker(self, i)])
            
            