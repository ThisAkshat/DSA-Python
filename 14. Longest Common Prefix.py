class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
Input: strs = ["flower","flow","flight"] res = ""

i = 0 (strs[0][0] = 'f')
s	check	result
"flower"	i==len(s)? 0==6 ❌ · s[0]!='f'? ❌	continue
"flow"	0==4 ❌ · 'f'!='f' ❌	continue
"flight"	0==6 ❌ · 'f'!='f' ❌	continue
Inner loop khatam → res += 'f' → res = "f"

i = 1 (strs[0][1] = 'l')
s	check	result
"flower"	1==6 ❌ · 'l'!='l' ❌	continue
"flow"	1==4 ❌ · 'l'!='l' ❌	continue
"flight"	1==6 ❌ · 'l'!='l' ❌	continue
→ res += 'l' → res = "fl"

i = 2 (strs[0][2] = 'o')
s	check	result
"flower"	2==6 ❌ · 'o'!='o' ❌	continue
"flow"	2==4 ❌ · 'o'!='o' ❌	continue
"flight"	2==6 ❌ · 'i' != 'o' ✅	return res
Output: "fl" ✅
"""
