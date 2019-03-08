// 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
// 他马上就写出了正确答案是100。但是他并不满足于此,
// 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
// 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
// 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

/**
 * 解题思路：连续字段的中部肯定是总数与某个数的商，同时还分这个除数的奇偶，以及左右序列的间距问题
 * 因此分为两种情况判断，通知注意Java除法向下取整的问题即可。
 */
import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>(); 
        int num = 2;
        while( 2*sum - num*num >= 0 ) {
            if( num % 2 == 0 ) {
                if (sum%num == num/2) {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    for (int i = (sum/num) - num/2 + 1; i <= (sum/num) + num/2; i++) {
                        temp.add(i);
                    }
                    result.add(0, temp);
                }
            } else {
                if (sum%num == 0) {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    for (int i = (sum/num) - num/2; i <= (sum/num) + num/2; i++) {
                        temp.add(i);
                    }
                    result.add(0, temp);
                }
            }
            num ++;
        }
        return result;
    }
}