class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = 0
        substring = ''

        if len(s) > 0:
            r = 1
            substring = s[0]

        for i in range(len(s)):

            j = 1
            l = 1
            while True:
                if i-j < 0 or i+j >= len(s):
                    break

                if s[i-j] == s[i+j]:
                    l += 2

                    if l > r:
                        r = l
                        substring = s[i-j:i+j+1]

                    j += 1

                else:
                    break

            j = 0
            l = 0
            while True:
                if i-j-1 < 0 or i+j >= len(s):
                    break

                if s[i+j] == s[i-j-1]:
                    l += 2

                    if l > r:
                        r = l
                        substring = s[i-j-1:i+j+1]

                    j += 1

                else:
                    break

        return substring

A = Solution()

print A.longestPalindrome("babad") == "bab"
print A.longestPalindrome("cbbd") == "bb"
print A.longestPalindrome("bbbb") == "bbbb"
print A.longestPalindrome("bbb") == "bbb"
print A.longestPalindrome("abc") == "a"
print A.longestPalindrome("a") == "a"
print A.longestPalindrome("") == ""
print A.longestPalindrome("racecar") == "racecar"
print A.longestPalindrome("rrrrreracecarered") == "reracecarer"
print A.longestPalindrome("crarracecarcarrab") == "racecar"
print A.longestPalindrome("abbaabbx") == "bbaabb"