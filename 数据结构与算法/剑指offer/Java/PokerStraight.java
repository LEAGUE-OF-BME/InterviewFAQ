public class Solution {
    public boolean isContinuous(int [] numbers) {
        // 5张牌，一定有一张是有花色
        int len = numbers.length;
        if (len < 5) return false;
        
        // 模仿一般的思路，先排序，然后将0插空看看
        for (int i = 0; i < len - 1; i++) {
            for (int j = i+1; j < len; j++){
                if (numbers[j] < numbers[i]) {
                    int tmp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = tmp;
                }
            }
        }
        // 统计0的个数
        int count = 0;
        for (int i = 0; i < len; i++) if (numbers[i] == 0) count++;
        
        // 判断从非0数开始，中间需不需要插入0以完成顺子，若需要则消耗0，最后0的数目不应该小于0
        for (int i = count + 1; i < len; i++) {
            if (numbers[i] - numbers[i-1] > 1) {
                count -= numbers[i] - numbers[i-1] - 1;
            } else if (numbers[i] - numbers[i-1] == 0) {
                return false;
            }
        }
        return count >= 0 ? true : false;
    }
}