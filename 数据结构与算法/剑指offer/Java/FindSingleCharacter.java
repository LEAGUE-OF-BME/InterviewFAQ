import java.util.HashMap;

public class Solution {
    public int FirstNotRepeatingChar(String str) {
        StringBuffer strbuf = new StringBuffer(str);
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        // 通过map记录每个字符出现的次数
        for (int i = 0; i < strbuf.length(); i++) {
            char c = strbuf.charAt(i);
            if (!map.containsKey(c)) {
                map.put(c, 1);
            } else {
                map.put(c, map.get(c) + 1);
            }
        }
        // 因为java map会排序，需要手动遍历找到最小的字符位置
        // indexOf 是返回第一个字符出现的位置
        int min = str.length() - 1;
        for (char c:map.keySet()){
            if (map.get(c) == 1) min = str.indexOf(c) < min ? str.indexOf(c) : min;
        }
        return min;
    }
}