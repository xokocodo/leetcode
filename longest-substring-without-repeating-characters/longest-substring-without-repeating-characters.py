class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        occurrences = {}
        longest_length = 0
        starting_point = 0
        i = 0

        while True:

            if i == len(s):
                break

            c = s[i]

            last_occurrence = occurrences.get(c)

            if last_occurrence != None and last_occurrence >= starting_point:
                # End of Valid Substring

                if i - starting_point > longest_length:
                    longest_length = i - starting_point

                starting_point = last_occurrence + 1

            else:
                occurrences[c] = i
                i += 1

        if len(s) - starting_point > longest_length:
            return len(s) - starting_point
        else:
            return longest_length


A = Solution()

print A.lengthOfLongestSubstring("abcabcbb") == 3
print A.lengthOfLongestSubstring("bbbbb") == 1
print A.lengthOfLongestSubstring("pwwkew") == 3
print A.lengthOfLongestSubstring("bbbbbbb") == 1
print A.lengthOfLongestSubstring("abcdef") == 6
print A.lengthOfLongestSubstring("aab") == 2
print A.lengthOfLongestSubstring("bba") == 6