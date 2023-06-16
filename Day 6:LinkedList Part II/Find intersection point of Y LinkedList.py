class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB
        
        while first!= second:
            first = headB if not first else first.next
            second = headA if not second else second.next
        
        return first