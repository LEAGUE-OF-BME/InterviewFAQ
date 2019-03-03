import java.util.ArrayList;

public class Solution {
    public int GetUglyNumber_Solution(int index) {
        
        if (index <= 0) return 0;
        if (index < 7) return index;
        
        ArrayList<Integer> uglyList = new ArrayList<Integer>();
        uglyList.add(1);
        
        int i2 = 0, i3 = 0, i5 = 0;
        
        // 丑数一定由另一个丑数x2或x3或x5得到
        while(uglyList.size() <= index) {
            int m2 = 2*uglyList.get(i2);
            int m3 = 3*uglyList.get(i3);
            int m5 = 5*uglyList.get(i5);
            int m = Math.min(m2, Math.min(m3,m5));
            if (m == m2) i2++;
            if (m == m3) i3++;
            if (m == m5) i5++;
            uglyList.add(m);
        }
        
        return uglyList.get(index - 1);
    }
}