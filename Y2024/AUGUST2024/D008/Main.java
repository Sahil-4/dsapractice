class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static int findMaxPathSum(TreeNode root, int res[]) {
        if (root == null)
            return 0;

        int lps = Math.max(0, findMaxPathSum(root.left, res));
        int rps = Math.max(0, findMaxPathSum(root.right, res));

        int tsum = root.val + lps + rps;
        res[0] = Math.max(res[0], tsum);

        return root.val + Math.max(lps, rps);
    }

    static int maxPathSum(TreeNode root) {
        int res[] = new int[1];
        res[0] = Integer.MIN_VALUE;

        findMaxPathSum(root, res);

        return res[0];
    }

    static void p1() {
        // Problem 1: Leetcode 124. Binary Tree Maximum Path Sum -
        // https://leetcode.com/problems/binary-tree-maximum-path-sum/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1

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

        int sum = maxPathSum(root);
        System.out.println(sum);
    }

    public static void main(String[] args) {
        // Day 9 of binary trees

        p1();
    }
}