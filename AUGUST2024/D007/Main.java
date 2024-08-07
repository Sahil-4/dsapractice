class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static int height(TreeNode root) {
        if (root == null)
            return 0;

        int lh = height(root.left);
        int rh = height(root.right);

        return Math.max(lh, rh) + 1;
    }

    static int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;

        int lh = height(root.left);
        int rh = height(root.right);

        // int d1 = lh + rh + 1; // for number of nodes
        int d1 = lh + rh; // for number of edges
        int d2 = diameterOfBinaryTree(root.left);
        int d3 = diameterOfBinaryTree(root.right);

        return Math.max(d1, Math.max(d2, d3));

        // Complexity analysis
        // Time : O(n ^ 2)
        // Space : O(1)
    }

    static void p1() {
        // Problem 1 : Leetcode 543. Diameter of Binary Tree -
        // https://leetcode.com/problems/diameter-of-binary-tree/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        // Tree strucutre 
        //       1
        //      /  \
        //    2    3
        //   / \    / \
        //  4  5 6  7

        int d = diameterOfBinaryTree(null);
        System.out.println(d);
    }

    public static void main(String[] args) {
        // Day 8 of binary tree

        p1();
    }
}
