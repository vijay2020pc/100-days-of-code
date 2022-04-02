Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

Solution:-
  
  class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                    return s[start+1:end+1]==s[start+1:end+1][::-1] or s[start:end]==s[start:end][::-1]
            start+=1
            end-=1
        return True
