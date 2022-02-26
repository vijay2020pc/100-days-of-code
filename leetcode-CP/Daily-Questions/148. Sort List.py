Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Solution:-
  class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        lst.sort()
        curr = head
        index = 0
        while curr:
            curr.val = lst[index]
            curr = curr.next
            index += 1
        return head
