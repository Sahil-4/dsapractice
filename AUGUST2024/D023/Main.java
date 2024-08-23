import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static List<Integer> inorderTraversal(TreeNode root) {
        // morris traversal
        // left root right
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        TreeNode curr = root;

        while (curr != null) {
            if (curr.left == null) {
                list.add(curr.val);
                curr = curr.right;
            } else {
                TreeNode rightest = curr.left;

                while (rightest.right != null && rightest.right != curr) {
                    rightest = rightest.right;
                }

                if (rightest.right == null) {
                    rightest.right = curr; // thread
                    curr = curr.left;
                } else {
                    list.add(curr.val);
                    rightest.right = null; // remove thread
                    curr = curr.right;
                }
            }
        }

        return list;
    }

    static void p1() {
        // Problem 1 : Leetcode 94. Binary Tree Inorder Traversal -
        // https://leetcode.com/problems/binary-tree-inorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/inorder-traversal/1

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

        List<Integer> list = inorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 24 of Binary Trees

        p1();
    }
}