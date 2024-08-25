import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 26 of Binary Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 114. Flatten Binary Tree to Linked List -
        // https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/binary-tree-to-dll/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        // flatten_Solution1(root);
        // flatten_Recursion(root);
        flatten(root);
        // TreeNode temp = flatten2DLL(root);

        TreeNode temp = root;
        while (temp != null) {
            System.out.println(temp.val);
            temp = temp.right;
        }
    }

    static void flatten_Solution1(TreeNode root) {
        if (root == null)
            return;

        Stack<TreeNode> stack = new Stack<>();
        TreeNode prev = root;

        if (prev.right != null)
            stack.push(prev.right);
        if (prev.left != null)
            stack.push(prev.left);

        while (!stack.isEmpty()) {
            TreeNode next = stack.pop();

            prev.left = null;
            prev.right = next;

            prev = prev.right;

            if (prev.right != null)
                stack.push(prev.right);
            if (prev.left != null)
                stack.push(prev.left);
        }

        // Complexity analysis
        // Time : O(n)
        // Space : O(w)
    }

    static TreeNode prev = null; // class variable

    static void flatten_Recursion(TreeNode root) {
        if (root == null)
            return;

        flatten(root.right);
        flatten(root.left);

        root.right = prev;
        root.left = null;

        prev = root;

        // Complexity analysis
        // Time : O(n)
        // Space : O(1) + Stack space for recursion
    }

    static void flatten(TreeNode root) {
        TreeNode curr = root;

        while (curr != null) {
            if (curr.left == null) {
                curr = curr.right;
            } else {
                TreeNode rightest = curr.left;
                while (rightest.right != null) {
                    rightest = rightest.right;
                }

                rightest.right = curr.right;
                curr.right = curr.left;
                curr.left = null;

                curr = curr.right;
            }
        }
    }

    static TreeNode head = null;

    TreeNode flatten2DLL(TreeNode root) {
        // Your code here
        prev = null;
        head = null;
        solve(root);
        return head;
    }

    static void solve(TreeNode root) {
        if (root == null)
            return;

        solve(root.left);

        if (prev == null) {
            head = root;
        } else {
            root.left = prev;
            prev.right = root;
        }

        prev = root;

        solve(root.right);
    }
}