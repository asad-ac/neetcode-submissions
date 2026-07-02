class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        # previous variable
        # first we can loop through linked list
        # store the current.next variable in nxt
        # current = prev
        # prev = current
        # current.next = nxt


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
