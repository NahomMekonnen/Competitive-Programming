class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1 :
            return word
        # words, n = [], len(word)
        # for i in range(n) :
        #     end = i + (n - numFriends) + 2 
        #     for j in range(i+1,end) :
        #         if j > n :
        #             break
        #         words.append(word[i:j])
        # words.sort()
        # return words[-1]
        largest, letter = 0, ""
        for i in range(len(word)) :
            if ord(word[i]) > largest :
                letter = word[i]
                largest = ord(word[i])
        end = (len(word) - numFriends) + 1
        words = []
        for i in range(len(word)) : 
            if word[i] == letter:
                if i + end >= len(word):
                    end = len(word)
                    words.append(word[i:end])
                else :
                    words.append(word[i:i+end])  
        words.sort()    
        return words[-1]
