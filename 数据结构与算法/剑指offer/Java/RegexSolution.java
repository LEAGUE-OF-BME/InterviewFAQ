/**
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
 */
public class Solution {
    public boolean match(char[] str, char[] pattern)
    {
        if (str == null || pattern == null ) return true;

        int strIndex = 0;
        int patternIndex = 0;
        
        return matchHelper(str, strIndex, pattern, patternIndex);
  }
    
   public boolean matchHelper(char[] str, int strIndex, char[] pattern, int patternIndex)
   {
      // 如果字符串和模式都匹配到头，则返回匹配成功
       if (strIndex >= str.length && patternIndex >= pattern.length) return true;
       // 如果模式先于字符串匹配完，则返回false
       if (strIndex < str.length && patternIndex >= pattern.length) return false;
       
       // 如果第二个字符为'*'，则进行前一个字符的比较
       // 1. 字符相等，（完全相等，或模式='.'） 则有三种选择：模式跳过此对+2，字符串向后走1，字符串和模式向后同时走位
       // 2. 字符串不相等，则模式跳过此对
       if (patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*') {
           if ( (strIndex != str.length && str[strIndex] == pattern[patternIndex]) 
               || (strIndex != str.length && pattern[patternIndex] == '.')) {
               return matchHelper(str, strIndex, pattern, patternIndex + 2) 
                   || matchHelper(str, strIndex + 1, pattern, patternIndex) 
                   || matchHelper(str, strIndex + 1, pattern, patternIndex + 2);
           } else {
               return matchHelper(str, strIndex, pattern, patternIndex + 2);
           }
       }
       // 如果模式和字符串相等（完全相等，或模式='.'），则模式和字符串向后跳1
       else if ( (strIndex != str.length && str[strIndex] == pattern[patternIndex]) 
               || (strIndex != str.length && pattern[patternIndex] == '.')) {
           return matchHelper(str, strIndex + 1, pattern, patternIndex + 1);
       }
       return false;
   }
}