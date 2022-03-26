Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

Solution:-
  class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index_map = {}
        stack = []
        
        for index, char in enumerate(s):
            last_index_map[char]=index
            
        for i in range(len(s)):
            if s[i] in stack:
                continue
                
            while stack and s[i]< stack[-1] and last_index_map[stack[-1]]>i:
                stack.pop()
                
            stack.append(s[i])
            
        return ''.join(stack)
