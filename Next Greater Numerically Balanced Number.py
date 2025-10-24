class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1,7777777) :
            cnt = Counter( list( str( i ) ) ) 
            broke = False
            for j in str(i) :
                if int(j) != cnt[ str(j) ] :
                    broke = True
                    break
            if not broke :
                return i
