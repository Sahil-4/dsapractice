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
    public static void main(String[] args) {
        // Day 27 of Binary Search Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 144. Binary Tree Preorder Traversal (Morris Traversal) -
        // https://leetcode.com/problems/binary-tree-preorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/preorder-traversal/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        List<Integer> list = preorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    static List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();

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
                    list.add(curr.val); // for pre 
                    rightest.right = curr;
                    curr = curr.left;
                } else {
                    // list.add(curr.val); // for in 
                    rightest.right = null;
                    curr = curr.right;
                }
            }
        }

        return list;
    }
}
