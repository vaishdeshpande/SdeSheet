class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        loop = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                loop = True
                break
        if loop == False:
            return None
        slow = head

        while fast!=slow:
            fast = fast.next
            slow = slow.next
        
        return fast