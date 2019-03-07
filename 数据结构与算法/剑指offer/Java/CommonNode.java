import java.util.ArrayList;
public class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) return null;
        ArrayList<ListNode> list = new ArrayList<ListNode>();
        while(pHead1 != null) {
            list.add(pHead1);
            pHead1 = pHead1.next;
        }
        while(pHead2 != null) {
            if (list.contains(pHead2)) return pHead2;
            pHead2 = pHead2.next;
        }
        return null;
    }
}

// 方法2
// 计算出两链表的长度差，即为交汇前的长度差，让多出的链表先走多出的长度，在一起向下遍历即可找到公共结点
class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) return null;
        int len1 = 0, len2 = 0;
        ListNode head1 = pHead1, head2 = pHead2;
        while (head1 != null) {
            len1++;
            head1 = head1.next;
        }
        while (head2 != null) {
            len2++;
            head2 = head2.next;
        }
        
        if (len1 >= len2) {
            for(int i = 0; i < len1-len2; i++) pHead1 = pHead1.next;
        } else {
            for(int i = 0; i < len2-len1; i++) pHead2 = pHead2.next;
        }
        
        while (pHead1 != null && pHead2 != null) {
            if (pHead1 == pHead2) return pHead1;
            pHead1 = pHead1.next; pHead2 = pHead2.next;
        }
        return null;
    }
}
