// 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
// 平衡二叉树是空树，或者左右两个子树的高度差不超过1的树
public class Solution {
    
    public int maxBranchNumber (TreeNode node, int depth) {
        if (node == null) return depth;
        return Math.max(maxBranchNumber(node.right, depth + 1), maxBranchNumber(node.left, depth + 1));
    }
    // 二叉树是很经典的可以用递归分析的数据结构
    // 每个结点下可以看做一个新的二叉树，判断其左右的最深深度是否相差大于1，若是，则不满足平衡的条件
    public boolean IsBalanced_Solution(TreeNode root) {
        
        if(root == null) return true;
        
        int right = maxBranchNumber(root.right, 1);
        int left = maxBranchNumber(root.left, 1);
        if (right > left + 1 || left > right + 1) return false;
        return IsBalanced_Solution(root.right) && IsBalanced_Solution(root.left);
    }
}