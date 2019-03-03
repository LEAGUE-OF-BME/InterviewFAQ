/**
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.ArrayList;
public class ReverseTheList03 {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        // 在最前面插入即可
        while(listNode != null) {
            result.add(0, listNode.val);
            listNode = listNode.next;
        }
        return result;
    }
}