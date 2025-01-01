class TreeNode {
    int val;

    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static int heightOfTree(TreeNode root) {
        if (root == null)
            return 0;

        int l = heightOfTree(root.left);
        int r = heightOfTree(root.right);

        return Math.max(l, r) + 1;
    }

    static boolean checkBalancedTree_Solution1(TreeNode root) {
        if (root == null)
            return true;

        int lh = heightOfTree(root.left);
        int rh = heightOfTree(root.right);

        if (Math.abs(lh - rh) > 1)
            return false;

        boolean lc = checkBalancedTree_Solution1(root.left);
        if (!lc)
            return false;

        boolean rc = checkBalancedTree_Solution1(root.right);

        return rc;
    }

    static int checkBalancedTree(TreeNode root) {
        if (root == null)
            return 0;

        int lh = checkBalancedTree(root.left);
        if (lh == -1)
            return -1;

        int rh = checkBalancedTree(root.right);
        if (rh == -1)
            return -1;

        if (Math.abs(lh - rh) > 1)
            return -1;

        return Math.max(lh, rh) + 1;
    }

    static boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;

        // return checkBalancedTree_Solution1(root);
        int n = checkBalancedTree(root);
        return n != -1;

        // Complexity analysis
        // Space : O(1), + auxiliory stack space for recrursion
        // Time : O(n ^ 2), O(n) to traverse each node and O(n) at each node to find
        // height of their left right sub tree
    }

    static void p1() {
        // Problem 1 : Leetcode 110. Balanced Binary Tree -
        // https://leetcode.com/problems/balanced-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1

        // Create the nodes
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        // Connect the nodes
        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // The tree structure now :
        // * 1
        // * / \
        // * 2 3
        // * / \
        // * 4 5

        boolean check = isBalanced(root);
        System.out.println(check);
    }

    public static void main(String[] args) {
        // Day 7 of Binary trees 

        p1();
    }
}