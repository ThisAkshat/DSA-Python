class Solution(object):
    def removeAnagrams(self, words):
        def isAna(S1, S2):
            return sorted(S1) == sorted(S2)

        r = []
        for i in words:
            if r and isAna(r[-1], i):
                continue
            r.append(i)
        return r


"""
2273. Find Resultant Array After Removing Anagrams

You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

 

Example 1:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.
"""



# Input: words = ["abba", "baba", "bbaa", "cd", "cd"]
#
# Step-by-step execution:
#
# 1. word = "abba"
#    r = [] (empty)
#    → Append "abba"
#    r = ["abba"]
#
# 2. word = "baba"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("baba")
#    "aabb" == "aabb" → True (anagram!)
#    → Skip "baba"
#    r = ["abba"]
#
# 3. word = "bbaa"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("bbaa")
#    "aabb" == "aabb" → True (anagram!)
#    → Skip "bbaa"
#    r = ["abba"]
#
# 4. word = "cd"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("cd")
#    "aabb" != "cd" → False (not anagram)
#    → Append "cd"
#    r = ["abba", "cd"]
#
# 5. word = "cd"
#    r = ["abba", "cd"]
#    Compare: sorted("cd") vs sorted("cd")
#    "cd" == "cd" → True (anagram - identical!)
#    → Skip "cd"
#    r = ["abba", "cd"]
#
# Final result: ["abba", "cd"] ✅
