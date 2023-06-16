class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head 
        groupPrev = dummyNode
        while True:
            kth = self.getKthNode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            prev , curr = kth.next,groupPrev.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummyNode.next

    
    def getKthNode(self,node,k):
        while node and k>0:
            node = node.next
            k = k-1
        return node