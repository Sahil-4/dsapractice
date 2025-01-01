class TreeNode {
    int val;

    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static int maxDepth(TreeNode root, int h) {
        if (root == null)
            return h;

        int a = maxDepth(root.left, h + 1);
        int b = maxDepth(root.right, h + 1);

        return Math.max(a, b);
    }

    static int maxDepth(TreeNode root) {
        return maxDepth(root, 0);
    }

    static void p1() {
        // Problem 1 : Leetcode 104. Maximum Depth of Binary Tree -
        // https://leetcode.com/problems/maximum-depth-of-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/height-of-binary-tree/1

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

        int d = maxDepth(root);
        System.out.println(d);
    }

    public static void main(String[] args) {
        // Day 6 of binary trees

        p1();
    }
}