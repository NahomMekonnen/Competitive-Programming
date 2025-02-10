# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cant, cnt = False, 0
        for word in words:
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    cant = True
                    break
            if not cant:
                cnt += len(word)
            cant = False
        return cnt