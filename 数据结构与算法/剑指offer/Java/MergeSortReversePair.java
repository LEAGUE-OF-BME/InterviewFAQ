/**
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 
即输出P%1000000007
 */
public class Solution {

    public int count = 0;

    public void merge(int[] array, int start, int end) { // ≥start <end
        if(start >= end-1 ) return;
        int mid = (start + end) >> 1;

        merge(array, start, mid);
        merge(array, mid, end);

        int left = mid - 1, right = end - 1;
        int[] copyArray = new int[end-start];
        int pos = end - start - 1;
        while (left >= start && right >= mid) {
            if (array[left] > array[right]) {
                copyArray[pos--] = array[left--];
                // Core: 每当前面的数大于后面，就记录为一个逆数对
                count += right - mid + 1;
            } else {
                copyArray[pos--] = array[right--];
            }
        }
        if (right < mid) {
            while(pos >= 0) copyArray[pos--] = array[left--];
        } else if (left < start) {
            while(pos >= 0) copyArray[pos--] = array[right--];
        }
        for (int i = 0; i < end-start; i++) array[start+i] = copyArray[i];
    }

    public int InversePairs(int [] array) {
        // 通过归并排序，几次置换位置，就有几个逆数对
        if (array.length == 0) return count;
        merge(array, 0, array.length);
        return count;
    }

    public static void main(String[] args) {
        int[] array = {364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575};
        Solution solution = new Solution();

        if (array.length == 0) System.out.println(solution.count);
        solution.merge(array, 0, array.length);
//        System.out.println(array);
//        for (int i=0; i < array.length ;i++ ) {
//            System.out.println(array[i]);
//        }
        System.out.println(solution.count);
    }
}
