You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

Solution:-
  
  class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k_begin is the k-th node from the beginning
        k_begin = head
        for _ in range(k-1):
            k_begin = k_begin.next
            
        # k_end is the k-th node from the end.
        # To find the k-th node from the end we use two pointers:
        # k_end and ptr which both point to head at the beginning
        k_end, ptr = head, head
        
        # we now create a k-distance between k_end and ptr
        for _ in range(k):
            ptr = ptr.next
            
        # now we keep traversing the linked list with ptr and, behind,
        # k_end. When ptr reaches the end (ptr == None), k_end is
        # pointing to the k-th node from the end
        while ptr:
            ptr = ptr.next
            k_end = k_end.next
            
        # now swap the values
        k_begin.val, k_end.val = k_end.val, k_begin.val
        
        return head
