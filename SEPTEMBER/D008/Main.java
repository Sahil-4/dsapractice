
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class HelperNode {
    public int height, minNode, maxNode;

    HelperNode(int height, int minNode, int maxNode) {
        this.height = height;
        this.minNode = minNode;
        this.maxNode = maxNode;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 8 of BST

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 99. Recover Binary Search Tree -
        // https://leetcode.com/problems/recover-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(7);
        root.left.right = new TreeNode(3);

        recoverTree(root);
    }

    static TreeNode first;
    static TreeNode middle;
    static TreeNode last;
    static TreeNode prev;

    static void fixBST(TreeNode root) {
        if (root == null)
            return;

        fixBST(root.left);

        if (root.val < prev.val) {
            if (first == null) {
                first = prev;
                middle = root;
            } else {
                last = root;
            }
        }

        prev = root;
        fixBST(root.right);
    }

    static void recoverTree(TreeNode root) {
        first = middle = last = null;
        prev = new TreeNode(Integer.MIN_VALUE);

        fixBST(root);

        if (first != null && last != null) {
            int temp = first.val;
            first.val = last.val;
            last.val = temp;
        } else if (first != null && middle != null) {
            int temp = first.val;
            first.val = middle.val;
            middle.val = temp;
        }

        // Complexity analysis
        // Time : O(n)
        // Space : O(1) + some global/instance variables
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Largest BST -
        // https://www.geeksforgeeks.org/problems/largest-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(7);
        root.left.right = new TreeNode(3);

        int s = largestBst(root);
        System.out.println(s);
    }

    static HelperNode largestBST(TreeNode root) {
        if (root == null) {
            return new HelperNode(0, Integer.MAX_VALUE, Integer.MIN_VALUE);
        }

        HelperNode l = largestBST(root.left);
        HelperNode r = largestBST(root.right);

        if (l.maxNode < root.val && r.minNode > root.val) {
            return new HelperNode(l.height + r.height + 1, Math.min(root.val, l.minNode),
                    Math.max(root.val, r.maxNode));
        }

        return new HelperNode(Math.max(l.height, r.height), Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    // Return the size of the largest sub-tree which is also a BST
    static int largestBst(TreeNode root) {
        // Write your code here
        if (root == null)
            return 0;

        HelperNode n = largestBST(root);
        return n.height;

        // Complexity analysis
        // Time : O(n)
        // Space : O(1) + O(n) for stack
    }
}