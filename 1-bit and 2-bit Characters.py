class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        b , i = [], 0
        while i < len(bits):
            if bits[i] == 1 :
                b.append(bits[i:i+2])
                i += 2
            else :
                b.append(bits[i])
                i += 1
        return b[-1] == 0
