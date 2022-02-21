Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

Solution:-
  class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            arr=[[1],[1,1]]
            cnt=numRows-2
            for i in range(cnt):
                temp=[1]
                for i in range(0,len(arr[-1])-1):
                    temp.append(arr[-1][i]+arr[-1][i+1])
                temp.append(1)
                arr.append(temp)
        return arr
