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
