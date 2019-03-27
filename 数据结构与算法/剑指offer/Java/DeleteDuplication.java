/**
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
 */
/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class DeleteDuplication {
    public ListNode deleteDuplication(ListNode pHead)
    {
        if (pHead == null) return null;
        // 模拟一个已经确定的链表开头
        ListNode result = new ListNode(pHead.val);
        // 下一个从pHead开始
        result.next = pHead;
        // lastHead指向一个确定唯一的链表结点。
        ListNode lastHead = result;
        
        while (pHead != null && pHead.next != null) {
            // 如果从此结点，开始后面有连续的相等结点，则找到下一个不连续的结点开始试探。
            if (pHead.val == pHead.next.val) {
                int val = pHead.val;
                ListNode tmp = pHead.next;
                while(tmp != null) {
                    if (tmp.val != val) break;
                    tmp = tmp.next;
                }
                pHead = tmp;
                lastHead.next = tmp;
            } else {
                // 如果不确定结点是独立的，则列为确定结点
                // 注意区分，当前结点和历史结点 
                lastHead = pHead;
                pHead = pHead.next;
            }
        }
        return result.next;
    }
}