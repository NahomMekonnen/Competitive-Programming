class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)
        counts = [0] * n
        count = 0
        for i in range(n) :
            if s[i] in vowels :
                count += 1
            counts[i] = count
        ans = 0
        # print(counts)
        for i in range(n - k + 1) :
            num_vowels = counts[i + k - 1] - counts[i - 1] if i > 0 else counts[i + k  - 1]
            # print(num_vowels, i + k - 1, i )
            ans = max(ans, num_vowels)
        return ans