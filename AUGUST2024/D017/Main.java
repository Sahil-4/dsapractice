
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static boolean checkTree(TreeNode root) {
        if (root == null)
            return true;
        if (root.left == null && root.right == null)
            return true;

        int sum = root.val;

        if (root.left != null)
            sum -= root.left.val;
        if (root.right != null)
            sum -= root.right.val;

        if (sum != 0)
            return false;

        boolean check1 = checkTree(root.left);
        if (!check1)
            return false;

        return checkTree(root.left);
    }

    static void p1() {
        // Problem 1 : Leetcode 2236. Root Equals Sum of Children -
        // https://leetcode.com/problems/root-equals-sum-of-children/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/children-sum-parent/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(1);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        boolean check = checkTree(root);
        System.out.println(check);
    }

    public static void main(String[] args) {
        // Day 18 of Binary Trees

        p1();
    }
}