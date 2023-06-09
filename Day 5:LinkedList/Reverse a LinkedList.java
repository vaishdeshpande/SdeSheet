
    class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) return head;
        ListNode node = head;
        ListNode prev = null;
        ListNode temp;
        while(node.next != null){
            temp = node.next;
            node.next  = prev;
            prev = node;
            node = temp;
        }
        node.next  = prev;
        return node;
    }
}


