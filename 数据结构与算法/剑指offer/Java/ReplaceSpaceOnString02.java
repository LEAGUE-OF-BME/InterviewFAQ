public class Solution {
    public String replaceSpace(StringBuffer str) {
       // 通过String/StringBuilder/StringBuffer中的replace(start, end, str)进行替换
       for (int i = 0; i < str.length(); i++) {
           if (str.charAt(i) == ' ' ) {
               str.replace(i, i+1, "%20");
           }
       }
       return str.toString();
    }
}