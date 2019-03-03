public class FindInTwoDimensionalArray01 {
    public boolean Find(int target, int [][] array) {
        int rowLength = array.length;
        if (rowLength == 0) return false;
        int columnLength = array[0].length;
        
        // 从二维数组的左下角开始找起
        // 原则是比当前点大往右找，比当前点小往上找
        int curRow = rowLength - 1;
        int curColumn = 0;
        
        while(curColumn < columnLength && curRow >= 0) {
            int val = array[curRow][curColumn];
            if (target == val) return true;
            else if (target < val) {
                curRow --;
            }
            else curColumn ++;
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] array = {{1,2,3,4,5}, {3,4,5,6,7}, {4,5,6,7,8}, {5,7,8,10,13}};
        int target1 = 7;
        int target2 = 20;
        FindInTwoDimensionalArray01 f = new FindInTwoDimensionalArray01();
        System.out.println(f.Find(target1, array)); // true
        System.out.println(f.Find(target2, array)); // false
    }
}