class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        len_list = 0 
        temp = None
        prev = None
        node = head
        while node!=None:
            node = node.next
            len_list = len_list + 1
        count = len_list//2


        while count>0 and head.next!=None:
            
            temp = head.next
            head.next = prev 
            prev = head
            head = temp
            count = count - 1
        if len_list%2!=0:
            head = head.next


        while prev!= None and head!= None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
        
        