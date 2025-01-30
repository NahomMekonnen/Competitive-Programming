# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    ans = ""
    for c in s:
        if c.islower():
            c = c.upper()
        else:
            c = c.lower()
        ans += c
    return ans